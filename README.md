📌 SUPER IMPORTANTE, LEER!
✅ 1. Crear la carpeta del proyecto
Abrir el explorador de archivos.

Crear una carpeta nueva llamada por ejemplo CALIA.

✅ 2. Abrir Visual Studio Code
Dentro de VS Code, hacer: File > Open Folder y abrir la carpeta CALIA.

✅ 3. Clonar el repositorio desde GitHub
Abrir la terminal de VS Code (Ctrl + ñ) y escribir:

git clone https://github.com/iariis/CALIA.git

Esto va a descargar el proyecto completo.
Luego, entrar a la carpeta del proyecto clonado:

cd CALIA

✅ 4. Crear y activar el entorno virtual (solo una vez)

python -m venv .venv
.\.venv\Scripts\activate

SIEMPRE TIENEN QUE CREARLO Y ACTIVARLO

✅ 5. Instalar pygame
Una vez activado el entorno:

pip install pygame
(Esto es lo único que necesitan instalar )

🔃 RAMAS Y TRABAJO INDIVIDUAL
✅ 6. Crear su propia rama

git checkout -b nombre-de-su-rama
Por ejemplo: git checkout -b lara

🚨 MUY IMPORTANTE SIEMPRE ANTES DE SUBIR ALGO PROBAR SI ANDA CON

app.py

lo que yo hice primero fué ver los videos pero él hace todo en app.py, nsotras debemos modulizar así que le mandé al chat para que me separara por archicos lo que hice

🚀 FLUJO PARA SUBIR CAMBIOS
Después de hacer sus partes:

git add .
git commit -m "Agregué [lo que hayan hecho]"
git push origin su-rama
🔁 Merge Final
Cuando todas hayan terminado, alguien que esté a cargo hace lo siguiente:

git checkout main
git pull origin main
git merge nombre-de-la-rama
git push origin main
Se repite ese proceso por cada rama que quieran fusionar.
