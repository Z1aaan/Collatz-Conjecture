from collatzer_main import *


def collatz_latex(collatz_N):
    latex_path = str()
    collatz_function_form = """
    f(n)=
    \\begin{cases}
    \\frac{n}{2}, & n \mod 2=0
    \\\\
    3n+1, &n \\mod 2=1
    \\end{cases} \\\\
    """
    latex_path += collatz_function_form

    print(latex_path)


if __name__ == "__main__":
    print("""Put messages here later""")
    collatz_latex(3)
