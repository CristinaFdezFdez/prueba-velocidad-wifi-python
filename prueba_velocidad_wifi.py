import speedtest

def imprimir_borde(titulo, ancho):
    print("╔" + "═" * (ancho - 2) + "╗")
    print("║" + titulo.center(ancho - 2) + "║")
    print("╠" + "═" * (ancho - 2) + "╣")

def imprimir_resultado(titulo, resultado, ancho):
    print("║" + titulo.ljust(ancho - 2) + "║")
    print("║" + resultado.rjust(ancho - 2) + "║")

def prueba_velocidad():
    print("Iniciando la prueba de velocidad...")

    # Crear una instancia del objeto Speedtest
    st = speedtest.Speedtest()
    
    # Obtener los servidores más cercanos
    st.get_best_server()
    
    # Medir la velocidad de descarga, subida y latencia
    print("\nRealizando la prueba de velocidad, por favor espere...\n")
    
    descarga = st.download() / 1_000_000  # Convertir de bits/s a Mbits/s
    subida = st.upload() / 1_000_000  # Convertir de bits/s a Mbits/s
    latencia = st.results.ping
    
    # Imprimir resultados con formato
    ancho = 40
    imprimir_borde(" RESULTADOS DE LA PRUEBA ", ancho)
    imprimir_resultado("Velocidad de descarga:", f"{descarga:.2f} Mbits/s", ancho)
    imprimir_resultado("Velocidad de subida:", f"{subida:.2f} Mbits/s", ancho)
    imprimir_resultado("Latencia:", f"{latencia} ms", ancho)
    print("╚" + "═" * (ancho - 2) + "╝")

if __name__ == "__main__":
    prueba_velocidad()
