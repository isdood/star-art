document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('pixelCanvas');
    const ctx = canvas.getContext('2d');
    const addFrameButton = document.getElementById('addFrame');
    const removeFrameButton = document.getElementById('removeFrame');
    const playAnimationButton = document.getElementById('playAnimation');

    let frames = [];
    let currentFrameIndex = 0;
    let isDrawing = false;
    let currentColor = '#000000';

    canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        drawPixel(e);
    });

    canvas.addEventListener('mousemove', (e) => {
        if (isDrawing) {
            drawPixel(e);
        }
    });

    canvas.addEventListener('mouseup', () => {
        isDrawing = false;
    });

    canvas.addEventListener('mouseleave', () => {
        isDrawing = false;
    });

    addFrameButton.addEventListener('click', () => {
        addFrame();
    });

    removeFrameButton.addEventListener('click', () => {
        removeFrame();
    });

    playAnimationButton.addEventListener('click', () => {
        playAnimation();
    });

    function drawPixel(e) {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const pixelSize = 10;

        ctx.fillStyle = currentColor;
        ctx.fillRect(Math.floor(x / pixelSize) * pixelSize, Math.floor(y / pixelSize) * pixelSize, pixelSize, pixelSize);
    }

    function addFrame() {
        const frame = ctx.getImageData(0, 0, canvas.width, canvas.height);
        frames.push(frame);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function removeFrame() {
        if (frames.length > 0) {
            frames.pop();
            if (frames.length > 0) {
                ctx.putImageData(frames[frames.length - 1], 0, 0);
            } else {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
        }
    }

    function playAnimation() {
        if (frames.length > 0) {
            let frameIndex = 0;
            const interval = setInterval(() => {
                ctx.putImageData(frames[frameIndex], 0, 0);
                frameIndex = (frameIndex + 1) % frames.length;
            }, 100);
            setTimeout(() => clearInterval(interval), frames.length * 100);
        }
    }
});
