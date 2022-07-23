BLTAssetManager:CreateEntry("units/menu/menu_scene/infamy_card_df", "texture", ModPath.."assets/units/menu/menu_scene/infamy_card_df.texture", nil)
BLTAssetManager:CreateEntry("units/menu/menu_scene/infamy_card", "object", ModPath.."assets/units/menu/menu_scene/infamy_card.object", nil)


function InfamyCardGui:show_rank(rank)
    self:clear_gui()

    self._data = {
        rank = rank
    }
	
	rank = rank - 1 --for our calculations

    if self._unit:damage() then
        self._unit:damage():run_sequence_simple("enable_card_blank")
    end
	
	local max_cards = 1690
	
    local icon_w = 200 --size of card on... the card?
    local icon_h = 300
	local width = 245 --size of the card on an atlas texture
	local height = 342
	
	local card = math.random(0, max_cards - 1)
	local image_index = math.fmod(card, 176)
	local pack_index = math.floor(card/176)
	local offset_x = math.fmod(card, 16) * width
	local offset_y = (math.floor(image_index / 16) * height)
    local yugioh_tcg = self._icon_gui:bitmap({
        x = 0,
        y = 0,
        blend_mode = "normal",
        texture = "units/menu/menu_scene/pack" .. pack_index,
        texture_rect = {
            offset_x,
            offset_y,
            width,
            height
        },
        color = Color.white,
        w = icon_w,
        h = icon_h
    })

    yugioh_tcg:set_render_template(Idstring("OverlayVertexColorTextured"))
end