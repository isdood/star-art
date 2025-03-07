class PixelArtTool:
    def __init__(self):
        self.canvas = []
        self.width = 16
        self.height = 16
        self.init_canvas()

    def init_canvas(self):
        self.canvas = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = color

    def get_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.canvas[y][x]
        return None

    def clear_canvas(self):
        self.init_canvas()

    def fill_canvas(self, color):
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x, y, color)

    def export_frame(self):
        return self.canvas

    def reimagine_with_ai(self, ai_model):
        canvas_array = np.array(self.canvas) / 255.0
        canvas_array = np.expand_dims(canvas_array, axis=0)
        ai_pixel_art = ai_model.predict(canvas_array)
        ai_pixel_art = np.squeeze(ai_pixel_art, axis=0)
        ai_pixel_art = (ai_pixel_art * 255).astype(np.uint8)
        self.canvas = ai_pixel_art.tolist()
