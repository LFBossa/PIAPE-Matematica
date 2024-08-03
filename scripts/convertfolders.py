from pathlib import Path


PROJECT_HOME = Path(__file__).parent.parent

DOCS_FOLDER = PROJECT_HOME / 'docs'

CREATE_SLIDES_FOLDERS = ['02-algebra', '03-equacoes', '04-funcoes']

def iterate_over_folders():
    for directory in CREATE_SLIDES_FOLDERS:
        modulo_folder = DOCS_FOLDER / directory
        for document in modulo_folder.glob(r"aula??.md"):
            yield document


def slides_filename(file: Path):
    return file.with_name(f"{file.stem}-slides{file.suffix}")


def check_if_slides_link_exists(file: Path):
    with open(file, 'r') as f:
        content = f.read()
    if "[Slides :material-presentation-play:]" in content:
        return True
    else:
        return False


def add_slides_questions_links(file: Path):
    if check_if_slides_link_exists(file):
        return
    else:
        slidesfile = slides_filename(file)
        slidesfilename = slidesfile.name
        filename = file.stem
        aulanumber = filename[4:6]
        linktoslides = f"[Slides :material-presentation-play:](./{slidesfilename})"
        linktoquestions = f"[Exercícios :writing_hand:](./questoes{aulanumber}.pdf)"
        print(f"Adding content to {file}")
        print(f"Adding {linktoslides} and {linktoquestions}")
        with open(file, 'a') as f:
            f.write("\n\n---\n\n")
            f.write('<div class="grid cards" markdown>\n')
            f.write(f" - {linktoslides}\n - {linktoquestions}\n")
            f.write("</div>\n")


def create_slides(file: Path):
    slidesfile = slides_filename(file)
    if slidesfile.exists():
        return
    else:
        print(f"Creating slides for {file}")
        with open(file, 'r') as f:
            content = f.read()
        with open(slidesfile, 'w') as f:
            header = "---\n"
            header += "template: reveal.html\n"
            header += "---\n"
            f.write( header )
            f.write( content )


if __name__ == '__main__':
    for file in iterate_over_folders():
        add_slides_questions_links(file)
        create_slides(file)
        break
            