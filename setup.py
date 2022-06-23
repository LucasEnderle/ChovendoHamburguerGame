import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="BurgerRain.py", icon="assets/burger.ico"
)]


cx_Freeze.setup(
    name="Burger Rain",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)