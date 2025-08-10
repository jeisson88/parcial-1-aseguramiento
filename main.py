from src.calidad import WebServiceModule, DataProcessingModule

def run_demo() -> None:
    ws = WebServiceModule(name="UsuariosAPI", owner="Equipo Backend", base_url="/api/v1/users")
    dp = DataProcessingModule(name="ETLFacturas", owner="Equipo Datos", batch_size=5000)

    ws.validate()
    dp.validate()

    ws.bump_version(minor=1)
    dp.bump_version(patch=1)

    print(ws.generate_docs())
    print(dp.generate_docs())


if __name__ == "__main__":
    run_demo()
