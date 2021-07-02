class Glass:
    content = 0
    capacity = 250

    def fill(self, ml):
        if Glass.capacity >= ml:
            Glass.content += ml
            Glass.capacity -= Glass.content
            return f'Glass filled with {Glass.content} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        Glass.content = 0 
        Glass.capacity = 250
        return 'Glass is now empty'

    def info(self):
        return f'{Glass.capacity} ml left'


