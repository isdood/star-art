class AnimationTool:
    def __init__(self):
        self.frames = []
        self.current_frame_index = 0

    def add_frame(self, frame):
        self.frames.append(frame)

    def remove_frame(self, index):
        if 0 <= index < len(self.frames):
            del self.frames[index]

    def play_animation(self):
        for frame in self.frames:
            self.display_frame(frame)

    def display_frame(self, frame):
        # Placeholder for displaying a frame
        pass

    def export_frames_as_pixel_art(self):
        # Placeholder for exporting frames as pixel art
        pass
