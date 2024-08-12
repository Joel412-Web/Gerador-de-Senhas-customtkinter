from cx_Freeze import setup, Executable
import sys

# Dependências adicionais que você pode precisar incluir
build_exe_options = {
    "packages": ["tkinter", "customtkinter", "random", "string", "pyperclip"],
    "include_files": []
}

# Configurações específicas do sistema
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para programas GUI (sem console)

# Configurações do executável
executables = [
    Executable(
        script="main1.py",  # Substitua com o nome do seu arquivo Python
        base=base,
        target_name="GeradorDeSenhas.exe",  # Nome do executável gerado
        icon=None  # Substitua com o caminho do ícone se desejar
    )
]

# Configuração do setup
setup(
    name="Gerador de Senhas",
    version="1.0",
    description="Um gerador de senhas simples",
    options={"build_exe": build_exe_options},
    executables=executables
)
