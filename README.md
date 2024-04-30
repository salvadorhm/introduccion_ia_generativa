# Introducción a la IA Generativa

## 0. Definiciones

### 0.1 IA Generativa

La IA generativa es un término que abarca cualquier tipo de inteligencia artificial diseñada para generar contenido nuevo y original en diversos dominios, no solo texto. Esto incluye la generación de imágenes, música, videos, entre otros tipos de datos.

### 0.2 Modelos de lenguaje grande

Los modelos de lenguaje largo son un subconjunto de la IA generativa, específicamente centrados en la generación de texto.

### 0.3 Herramientas para gestionar modelos de lenguaje grande de forma local

Una forma de utilizar los modelos de lenguaje grande de forma local es mediante el uso de herramientas que permitan descargar y gestionar estos modelos. Existen una gran variedad de herramientas dependiendo del uso que se desea tener, entre las principales se encuentran las siguientes:

| No | Nombre | Descripción |
| -- | -- | -- |
| 1 | [GPT4ALL](https://gpt4all.io/index.html) | Es una herramienta para tener un chatBot libre ejecutandose de forma local sin necesidad de internet |
| 2 | [ollama](https://ollama.com/) | Es una herramienta que permite gestionar modelos de lenguaje largo de forma local, para interactuar con ellos y poder desarrollar aplicaciones que hagan uso de estos modelos, mediante un servidor y el uso de API REST |
| 3 | [LM Studio](https://lmstudio.ai/) | Es una herrameinta que permite desacargar y ejecutar modelos de lenguaje grande de forma local, permite interactuar con ellos mediante un chatBot, además de montar un servidor basado en la API libre de [OpenAI](https://platform.openai.com/docs/api-reference). |
| 4 | [JAN](https://jan.ai/about) | Es una herramienta alternativa de código abierto para ejecuar ChatGPT de [OpenAI](https://platform.openai.com/docs/api-reference). |



# ollama

## 1. Instalación de ollama

En este curso se utilizará [ollama](https://ollama.com/), que es una herramienta que permite ejecutar modelos de lenguaje largo, además de permitir descagar, entrenar y generar nuevos modelos.

Pasos para la instalación de [ollama](https://ollama.com/) en Linux, macOS y Windows.

```bash
$curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Puesta en marcha

Una vez que se descargo e instalo [ollama](https://ollama.com/) se puede iniciar y detener su ejecución para que no se ejecute en segundo plano.

Para iniciar el servidor se ejecuta el siguiente comando:

```bash
$ollama serve
```

## 3. Lista de modelos disponibles

En la seccion de modelos de [ollama](https://ollama.com/), hay una lista de [modelos](https://ollama.com/library) disponibles para utilizarse, cada modelo tiene una descripción y diferentes versiones (tags) disponibles, estas versiones varian en tamaño, uso, idiomas, y capacidad de responder preguntas.

| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| Llama 2            | 7B         | 3.8GB | `ollama run llama2:7b`            |
| Mistral            | 7B         | 4.1GB | `ollama run mistral:7b`           |
| Dolphin Phi        | 2.7B       | 1.6GB | `ollama run dolphin-phi`       |
| Phi-2              | 2.7B       | 1.7GB | `ollama run phi`               |
| Neural Chat        | 7B         | 4.1GB | `ollama run neural-chat`       |
| Starling           | 7B         | 4.1GB | `ollama run starling-lm`       |
| Code Llama         | 7B         | 3.8GB | `ollama run codellama`         |
| Llama 2 Uncensored | 7B         | 3.8GB | `ollama run llama2-uncensored` |
| Llama 2 13B        | 13B        | 7.3GB | `ollama run llama2:13b`        |
| Llama 2 70B        | 70B        | 39GB  | `ollama run llama2:70b`        |
| Orca Mini          | 3B         | 1.9GB | `ollama run orca-mini`         |
| Vicuna             | 7B         | 3.8GB | `ollama run vicuna`            |
| LLaVA              | 7B         | 4.5GB | `ollama run llava`             |
| Gemma              | 2B         | 1.4GB | `ollama run gemma:2b`          |
| Gemma              | 7B         | 4.8GB | `ollama run gemma:7b`          |
| Solar              | 10.7B      | 6.1GB | `ollama run solar`             |

## 4. Descargar imagenes

Antes de iniciar hay que descargar un modelo para comenzar a interactuar como el, para este proceso se ejeucta el siguiente comando:

```bash
$ollama pull llama2
```

## 5. Ver modelos descagados

Una vez que se descargan los modelos es posible ver los modelos que estan en el servidor local para poder utilzarlos.

```bash
$ollama list
```

### 5.1 Ejemplo de lista de modelos

| NAME | ID | SIZE | MODIFIED |
| -- | -- | -- | -- |
| llama2:latest| 78e26419b446 | 3.8 GB | 37 hours ago |
| orca-mini:3b | 2dbd9f439647 | 2.0 GB | 37 hours ago |
| phi:latest | e2fd6321a5fe | 1.6 GB | 37 hours ago |
| tinyllama:latest | 2644915ede35 | 637 MB | 37 hours ago |

## 6. Ejecutar modelo

Con los modelos descagados localmente es posible interactuar con ellos de dos formas, como se muestra a continuación:

### 6.1 Modo de 1 consulta

En el modo de consulta se realiza una llamada al modelo y se anexa una pregunta, este generará una respuesta y la imprimira en consola.

```bash
$ollama run llama2 ¿porqué el cielo es azúl?
```

### 6.2 Modo interactivo

```bash
$ollama run llama2
```
