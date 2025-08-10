from calidad import (
    WebServiceModule,
    DataProcessingModule,
    InMemoryRepository,
    UserService,
)

def run_demo() -> None:
    ws = WebServiceModule(name="UsuariosAPI", owner="Equipo Backend", base_url="/api/v1/users")
    dp = DataProcessingModule(name="ETLFacturas", owner="Equipo Datos", batch_size=5000)

    repo = InMemoryRepository(name="RepoMem", owner="Equipo Datos")
    service = UserService(name="ServicioUsuarios", owner="Equipo Backend", repo=repo)

    # Validaciones
    for comp in (ws, dp, repo, service):
        comp.validate()

    # Usar servicio + repositorio
    service.register_user("u1", {"email": "ana@example.com", "nombre": "Ana"})
    print("Usuario u1:", service.get_user("u1"))

    # Versiones y docs
    for comp in (ws, dp, repo, service):
        comp.bump_version(minor=1)
        print(comp.generate_docs())

if __name__ == "__main__":
    run_demo()
