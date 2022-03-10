import click

from PIL import Image, ImageSequence

@click.command()
@click.option('--output-path', help='Output path', required=True)
@click.option('--gif-path', help='GIF path', required=True)
@click.option('--bg-path', help='Background image path', required=True)
@click.option('--fit-origin', help='Resize background image from GIF', is_flag=True)
@click.option('--debug', help='Save to png each frame', is_flag=True)
def gif_composite(output_path, gif_path, bg_path, fit_origin, debug):
    gif = Image.open(gif_path)
    bg = Image.open(bg_path)

    if fit_origin:
        bg = bg.resize(gif.size)

    frames = []
    index = 0
    loop = -1

    for frame in ImageSequence.Iterator(gif):
        if 'loop' in frame.info:
            loop = frame.info['loop']

        compose = bg.copy()
        compose.paste(frame, frame.convert('RGBA'))

        # NOTE(JJO): For debugging
        if debug:
            compose.save(f"output{index}.png")
            index += 1
        
        frames.append(compose)

    # NOTE(JJO): duration은 1000ms 기준
    duration = gif.info['duration'] * gif.n_frames / 1000

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=duration, loop=loop, optimise=False, format='GIF')

if __name__ == '__main__':
    gif_composite()
