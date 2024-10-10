from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

def programa():
    # Configurar opciones de Chrome
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    # Inicializar el driver de Chrome con WebDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),  # Instalar automáticamente el ChromeDriver
        options=opts
    )

    # URL de la página que contiene la tabla
    url = 'https://www.nfl.com/stats/team-stats/'
    driver.get(url)

    # Esperar a que aparezca el botón de las cookies
    try:
        # Esperar hasta 10 segundos a que el botón de cookies sea clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[2]/div/div[2]/button'))
        ).click()  # Clickea el botón de cookies
    except Exception as e:
        print("No se pudo encontrar o hacer clic en el botón de cookies:", e)

    # Esperar un momento para que la tabla se cargue
    sleep(4)

    # Seleccionar la tabla
    table = driver.find_element(By.XPATH, '/html/body/div[3]/main/section[3]/div/div/div/table')
    # Extraer todas las filas de la tabla
    rows = table.find_elements(By.TAG_NAME, 'tr')
    #encabezados
    encabezados = driver.find_elements(By.XPATH, '/html/body/div[3]/main/section[3]/div/div/div/table/thead/tr/th')
    # Crear una lista para almacenar los datos de la tabla
    table_data = []

    # Iterar sobre las filas y extraer las columnas (celdas)
    for row in rows:
        # Extraer las columnas de la fila
        cols = row.find_elements(By.TAG_NAME, 'td')
        # Guardar los valores de las columnas en una lista
        cols = [col.text for col in cols]
        # Agregar la fila a table_data
        table_data.append(cols)

    # Convertir la lista en un DataFrame de Pandas
    df = pd.DataFrame(table_data)
    df = df.drop(0)
    #insertar encabezados:
    tabla_final={}
    for i, thx in enumerate(encabezados):
        tabla_final[thx.text]=df[i]
    df1 = pd.DataFrame(tabla_final)
    # Imprimir o guardar el DataFrame
    return(df1)

def sumate():
    return 2+4+5+6
