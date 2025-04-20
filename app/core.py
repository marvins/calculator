

class Icon_Set:

    ARROW_LEFT  = 0
    ARROW_RIGHT = 1
    ARROW_UP    = 2
    ARROW_DOWN  = 3
    ARROWS_ALL  = 4
    ENTER       = 5
    ESCAPE      = 6

    @staticmethod
    def icon_tag( value ):

        if value == Icon_Set.ARROW_LEFT:
            return 'arrow_left_30'
        if value == Icon_Set.ARROW_RIGHT:
            return 'arrow_right_30'
        if value == Icon_Set.ARROW_UP:
            return 'arrow_up_30'
        if value == Icon_Set.ARROW_DOWN:
            return 'arrow_down_30'
        if value == Icon_Set.ARROWS_ALL:
            return 'arrows_all_16'
        if value == Icon_Set.ENTER:
            return 'enter_16'
        if value == Icon_Set.ESCAPE:
            return 'escape_16'