import sys

from rede import teste_conexao, teste_dns
from sistema import usuario_conectado, mostrar_ip, OS
from logger import salvar_log
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

console = Console()


def limpar_tela() -> None:
    """Limpa a tela."""
    console.clear()


def pausar() -> None:
    input("\nPressione ENTER para continuar...")


def status_color(status: bool) -> str:
    """Retorna status colorido."""
    return "[green]✓ OK[/green]" if status else "[red]✗ ERRO[/red]"


def cabecalho() -> None:
    console.print(
        Panel.fit(
            "[bold cyan]Ferramenta de Diagnóstico de Rede[/bold cyan]\n"
            "[dim]Projeto de estudos - Python[/dim]"
        )
    )


def menu() -> None:
    console.print("\n[bold]Menu[/bold]")
    console.print("1 - Testar conexão")
    console.print("2 - Identificar IP local")
    console.print("3 - Testar DNS")
    console.print("4 - Usuário conectado")
    console.print("5 - OS")
    console.print("6 - Diagnóstico completo")
    console.print("0 - Sair")


def diagnostico_completo() -> None:
    limpar_tela()
    cabecalho()

    salvar_log("Diagnóstico completo iniciado")

    internet, latencia = teste_conexao()
    ip = mostrar_ip()
    dns = teste_dns()
    usuario = usuario_conectado()
    sistema_operacional = OS()

    table = Table(title="Resultado do Diagnóstico")

    table.add_column("Item", style="cyan")
    table.add_column("Status")
    table.add_column("Detalhe")

    table.add_row("Internet", status_color(internet), str(latencia))
    table.add_row("IP Local", "[blue]INFO[/blue]", str(ip))
    table.add_row("DNS", status_color(dns), "Resolução de nomes")
    table.add_row("Usuário", "[blue]INFO[/blue]", str(usuario))
    table.add_row("OS", "[blue]INFO[/blue]", str(sistema_operacional))

    console.print(table)

    salvar_log("Diagnóstico completo finalizado")
    pausar()


def main() -> None:
    salvar_log("Aplicação iniciada")

    try:
        while True:
            limpar_tela()
            cabecalho()
            menu()

            opcao = input("\n► Escolha uma opção: ").strip()

            if opcao == "1":
                limpar_tela()
                cabecalho()

                salvar_log("Teste de conexão executado")
                internet, latencia = teste_conexao()

                console.print("\n[bold]Teste de Conexão[/bold]")
                console.print(f"Status: {status_color(internet)}")
                console.print(f"Latência: {latencia}")

                pausar()

            elif opcao == "2":
                limpar_tela()
                cabecalho()

                salvar_log("IP local solicitado")
                ip = mostrar_ip()

                console.print("\n[bold]IP Local[/bold]")
                console.print(f"Endereço: [yellow]{ip}[/yellow]")

                pausar()

            elif opcao == "3":
                limpar_tela()
                cabecalho()

                salvar_log("Teste de DNS executado")
                dns_status = teste_dns()

                console.print("\n[bold]Teste de DNS[/bold]")
                console.print(f"Status: {status_color(dns_status)}")

                pausar()

            elif opcao == "4":
                limpar_tela()
                cabecalho()

                salvar_log("Usuário conectado solicitado")
                usuario = usuario_conectado()

                console.print("\n[bold]Usuário Conectado[/bold]")
                console.print(f"Nome: [yellow]{usuario}[/yellow]")

                pausar()


            elif opcao == "5":
                limpar_tela()
                cabecalho()

                salvar_log("Detecção de OS iniciada")
                sistema_operacional = OS()

                console.print("\n[bold]OS detectado[/bold]")
                console.print(f"OS: [blue]{sistema_operacional}[/blue]") 

                pausar()  


            elif opcao == "6":
                diagnostico_completo()

            elif opcao == "0":
                limpar_tela()
                console.print("[green]Encerrando aplicação...[/green]")
                salvar_log("Aplicação encerrada normalmente")
                sys.exit(0)

            else:
                console.print("[red]Opção inválida![/red]")
                pausar()

    except KeyboardInterrupt:
        console.print("\n[yellow]Programa encerrado com CTRL+C[/yellow]")
        salvar_log("Aplicação interrompida pelo usuário")
        sys.exit(0)

    except Exception as e:
        console.print(f"[red]Erro inesperado: {e}[/red]")
        salvar_log(f"Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()