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

Para esta parte del curso se basa en la documentación del repositorio de [ollama github](https://github.com/ollama/ollama)

## 1. Instalación de ollama

Para realizar la instalación de ollama se debe descargar la versión que corresponda al sistema operativo que se utiliza (Linux, macOS y Windows), esto se hace en la página oficial de [ollama download](https://ollama.com/download) en Linux, macOS y Windows.

### 1.1 Instalación en GNU Linux

```bash
$curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Puesta en marcha

Una vez que se descargo e instalo [ollama](https://ollama.com/) se puede iniciar y detener su ejecución para que no se ejecute en segundo plano.

Para iniciar el servidor se ejecuta el siguiente comando:

```bash
$ollama serve
```

Nota: al ejeuctar el servidor este habilita un servicio en **http://localhost:11434**, al que se puede acceder de diferentes formas, como se vera posteriormente.

### 2.1 Ejemplo de ejecución del servidor cuando se usa solo la CPU

```bash
time=2024-04-30T15:06:53.323Z level=INFO source=images.go:817 msg="total blobs: 5"
time=2024-04-30T15:06:53.323Z level=INFO source=images.go:824 msg="total unused blobs removed: 0"
time=2024-04-30T15:06:53.324Z level=INFO source=routes.go:1143 msg="Listening on 127.0.0.1:11434 (version 0.1.32)"
time=2024-04-30T15:06:53.324Z level=INFO source=payload.go:28 msg="extracting embedded files" dir=/tmp/ollama523635885/runners
time=2024-04-30T15:06:56.217Z level=INFO source=payload.go:41 msg="Dynamic LLM libraries [cpu_avx cpu_avx2 cuda_v11 rocm_v60002 cpu]"
time=2024-04-30T15:06:56.217Z level=INFO source=gpu.go:121 msg="Detecting GPU type"
time=2024-04-30T15:06:56.217Z level=INFO source=gpu.go:268 msg="Searching for GPU management library libcudart.so*"
time=2024-04-30T15:06:56.218Z level=INFO source=gpu.go:314 msg="Discovered GPU libraries: [/tmp/ollama523635885/runners/cuda_v11/libcudart.so.11.0]"
time=2024-04-30T15:06:56.218Z level=INFO source=gpu.go:343 msg="Unable to load cudart CUDA management library /tmp/ollama523635885/runners/cuda_v11/libcudart.so.11.0: your nvidia driver is too old or missing, please upgrade to run ollama"
time=2024-04-30T15:06:56.219Z level=INFO source=gpu.go:268 msg="Searching for GPU management library libnvidia-ml.so"
time=2024-04-30T15:06:56.220Z level=INFO source=gpu.go:314 msg="Discovered GPU libraries: []"
time=2024-04-30T15:06:56.220Z level=INFO source=cpu_common.go:11 msg="CPU has AVX2"
time=2024-04-30T15:06:56.220Z level=INFO source=routes.go:1164 msg="no GPU detected"
```

### 2.2 Ejemplo de ejecución del servidor cuando se utiliza GPU

```bash
pendiente
```

### 2.3 Ejemplo de ejecución cuando recibe una petición

```bash
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":57132,"status":200,"tid":"140145076446784","timestamp":1714489663}
{"function":"process_single_task","level":"INFO","line":1506,"msg":"slot data","n_idle_slots":1,"n_processing_slots":0,"task_id":2,"tid":"140147531671424","timestamp":1714489663}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":57136,"status":200,"tid":"140145237952064","timestamp":1714489663}
{"function":"process_single_task","level":"INFO","line":1506,"msg":"slot data","n_idle_slots":1,"n_processing_slots":0,"task_id":3,"tid":"140147531671424","timestamp":1714489663}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":36780,"status":200,"tid":"140145271522880","timestamp":1714489663}
{"function":"process_single_task","level":"INFO","line":1506,"msg":"slot data","n_idle_slots":1,"n_processing_slots":0,"task_id":4,"tid":"140147531671424","timestamp":1714489663}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":36784,"status":200,"tid":"140145246344768","timestamp":1714489663}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":36788,"status":200,"tid":"140145263130176","timestamp":1714489663}
{"function":"process_single_task","level":"INFO","line":1506,"msg":"slot data","n_idle_slots":1,"n_processing_slots":0,"task_id":5,"tid":"140147531671424","timestamp":1714489663}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":36788,"status":200,"tid":"140145263130176","timestamp":1714489663}
{"function":"launch_slot_with_data","level":"INFO","line":830,"msg":"slot is processing task","slot_id":0,"task_id":6,"tid":"140147531671424","timestamp":1714489663}
{"function":"update_slots","ga_i":0,"level":"INFO","line":1809,"msg":"slot progression","n_past":0,"n_past_se":0,"n_prompt_tokens_processed":18,"slot_id":0,"task_id":6,"tid":"140147531671424","timestamp":1714489663}
{"function":"update_slots","level":"INFO","line":1836,"msg":"kv cache rm [p0, end)","p0":0,"slot_id":0,"task_id":6,"tid":"140147531671424","timestamp":1714489663}
{"function":"print_timings","level":"INFO","line":269,"msg":"prompt eval time     =    1442.30 ms /    18 tokens (   80.13 ms per token,    12.48 tokens per second)","n_prompt_tokens_processed":18,"n_tokens_second":12.480092519085876,"slot_id":0,"t_prompt_processing":1442.297,"t_token":80.12761111111111,"task_id":6,"tid":"140147531671424","timestamp":1714489668}
{"function":"print_timings","level":"INFO","line":283,"msg":"generation eval time =    3389.28 ms /    22 runs   (  154.06 ms per token,     6.49 tokens per second)","n_decoded":22,"n_tokens_second":6.491046486514556,"slot_id":0,"t_token":154.05836363636365,"t_token_generation":3389.284,"task_id":6,"tid":"140147531671424","timestamp":1714489668}
{"function":"print_timings","level":"INFO","line":293,"msg":"          total time =    4831.58 ms","slot_id":0,"t_prompt_processing":1442.297,"t_token_generation":3389.284,"t_total":4831.581,"task_id":6,"tid":"140147531671424","timestamp":1714489668}
{"function":"update_slots","level":"INFO","line":1640,"msg":"slot released","n_cache_tokens":40,"n_ctx":2048,"n_past":39,"n_system_tokens":0,"slot_id":0,"task_id":6,"tid":"140147531671424","timestamp":1714489668,"truncated":false}
{"function":"log_server_request","level":"INFO","line":2734,"method":"POST","msg":"request","params":{},"path":"/completion","remote_addr":"127.0.0.1","remote_port":36788,"status":200,"tid":"140145263130176","timestamp":1714489668}
{"function":"process_single_task","level":"INFO","line":1506,"msg":"slot data","n_idle_slots":1,"n_processing_slots":0,"task_id":31,"tid":"140147531671424","timestamp":1714489668}
{"function":"log_server_request","level":"INFO","line":2734,"method":"GET","msg":"request","params":{},"path":"/health","remote_addr":"127.0.0.1","remote_port":36802,"status":200,"tid":"140145254737472","timestamp":1714489668}
{"function":"log_server_request","level":"INFO","line":2734,"method":"POST","msg":"request","params":{},"path":"/tokenize","remote_addr":"127.0.0.1","remote_port":36802,"status":200,"tid":"140145254737472","timestamp":1714489668}
[GIN] 2024/04/30 - 15:07:48 | 200 |  7.046967594s |       127.0.0.1 | POST     "/api/generate"
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
$ollama pull gemma:2b
```

Ejemplo de desacarga del modelo gemma:2b

```bash
pulling manifest 
pulling c1864a5eb193... 100% ▕█████████████████████████████████████████████████████████████████████▏ 1.7 GB                         
pulling 097a36493f71... 100% ▕█████████████████████████████████████████████████████████████████████▏ 8.4 KB                         
pulling 109037bec39c... 100% ▕█████████████████████████████████████████████████████████████████████▏  136 B                         
pulling 22a838ceb7fb... 100% ▕█████████████████████████████████████████████████████████████████████▏   84 B                         
pulling 887433b89a90... 100% ▕█████████████████████████████████████████████████████████████████████▏  483 B                         
verifying sha256 digest 
writing manifest 
removing any unused layers 
success 
```

## 5. Ver modelos descagados

Una vez que se descargan los modelos es posible ver los modelos que estan en el servidor local para poder utilzarlos.

```bash
$ollama list
```

### 5.1 Ejemplo de lista de modelos

| NAME | ID | SIZE | MODIFIED |
| -- | -- | -- | -- |
| gemma:2b | b50d6c999e59 | 1.7 GB | 41 seconds ago |

## 6. Ejecutar modelo

Con los modelos descagados localmente es posible interactuar con ellos de varias formas, como se muestra a continuación:

### 6.1 Modo de 1 consulta en terminal

En el modo de consulta se realiza una llamada al modelo y se anexa una pregunta, este generará una respuesta y la imprimira en consola.

```bash
$ollama run gemma:2b ¿porqué el cielo es azúl?
```

Ejemplo de salida

```bash
El cielo no es azúl. El cielo es azul porque las longitudes de onda del azul son más largas que las longitudes de onda del rojo. Esto significa que la luz azul está menos dispersada en el aire, lo que significa que está más estable y aparece azul.
```

### 6.2 Modo interactivo en terminal

```bash
$ollama run gemma:2b
```

Ejemplo de salida

```bash
>>> ¿porqué el cielo es azúl?
El cielo no es azúl. El cielo es azul debido a que la luz solar atrae las longitudes de onda más cortas en la atmósfera, como el azul y el verde.

>>> Send a message (/? for help)
```

Nota: Para salir del modo interactivo se utliza la combinación de teclas **Ctrl + d**.

### 6.3 Mediante consulta de la API REST con curl sin parámetros (Generación de respuesta)

Consulta simple sin parámetros:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt":"¿porqué el cielo es azúl?"
}'
```

Ejemplo de salida

```bash
{"model":"gemma:2b","created_at":"2024-04-30T15:18:52.51818509Z","response":"El","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:52.695474933Z","response":" cielo","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:52.798268348Z","response":" no","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:52.907026682Z","response":" es","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.019430275Z","response":" az","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.196500878Z","response":"úl","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.298319953Z","response":".","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.400066568Z","response":" El","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.501729123Z","response":" cielo","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.620523445Z","response":" es","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.807266717Z","response":" azul","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:53.92047312Z","response":" porque","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.106861762Z","response":" contiene","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.225510424Z","response":" más","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.408772977Z","response":" azul","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.52286666Z","response":" que","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.695894974Z","response":" cualquier","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.815171036Z","response":" otro","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:54.996691939Z","response":" color","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:55.117217561Z","response":" del","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:55.311956601Z","response":" espectro","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:55.513452331Z","response":" visible","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:55.71979871Z","response":".","done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:18:55.909744051Z","response":"","done":true,"context":[106,1645,108,235737,1276,14419,822,34327,875,4722,27026,235336,107,108,106,2516,108,3275,34327,793,875,4722,27026,235265,2810,34327,875,13788,10755,37550,3267,13788,907,16377,14207,2881,1177,198706,12918,235265,107,108],"total_duration":6576316703,"load_duration":1781189742,"prompt_eval_count":18,"prompt_eval_duration":1362568000,"eval_count":24,"eval_duration":3391382000}
```

### 6.4 Mediante consulta de la API REST con curl con parámetros (Generación de respuesta)

Consulta utilizando el parámetro stream

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt":"¿porqué el cielo es azúl?",
  "stream" : false
}'
```

Como se puede ver en la salida, el resultado no se va mostrando palabra por palabra, sólo se muestra el resultado final.

Ejemplo de salida:

```bash
{"model":"gemma:2b","created_at":"2024-04-30T15:24:38.823431957Z","response":"El cielo no es azúl. El cielo es azul debido al efecto de Rayleigh. El efecto Rayleigh es una propiedad de la luz que establece que la luz más corta (como el azul) se dispersa más fácilmente por un medio que tiene un tamaño comparable al de las partículas del medio. El cielo está formado por el azul del universo, que es una mezcla de diferentes longitudes de onda de luz.","done":true,"context":[106,1645,108,235737,1276,14419,822,34327,875,4722,27026,235336,107,108,106,2516,108,3275,34327,793,875,4722,27026,235265,2810,34327,875,13788,34355,717,41064,581,153902,235265,2810,41064,153902,875,1749,43182,581,683,16601,907,99334,907,683,16601,3267,46326,591,14197,822,13788,235275,699,58989,235250,3267,69360,1395,748,15716,907,8819,748,33064,28477,717,581,1778,152737,1177,15716,235265,2810,34327,5365,104099,1395,822,13788,1177,68905,235269,907,875,1749,59619,581,17340,29717,484,581,73227,581,16601,235265,107,108],"total_duration":7129292361,"load_duration":2006890139,"prompt_eval_count":18,"prompt_eval_duration":575924000,"eval_count":82,"eval_duration":4499467000}
```

### 6.5 Mediante consulta de la API REST con curl sin parámetros (Modo Chat)

Consulta simple sin parámetros:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma:2b",
  "messages": [
    { "role": "user", "content": "¿porqué el cielo es azúl?" }
  ]
}'
```

Ejemplo de salida

```bash
{"model":"gemma:2b","created_at":"2024-04-30T15:29:05.42156699Z","message":{"role":"assistant","content":"El"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:05.622209069Z","message":{"role":"assistant","content":" cielo"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:05.913998916Z","message":{"role":"assistant","content":" no"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:06.294631829Z","message":{"role":"assistant","content":" es"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:06.412776811Z","message":{"role":"assistant","content":" az"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:06.528744984Z","message":{"role":"assistant","content":"úl"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:06.708626937Z","message":{"role":"assistant","content":"."},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:06.894168579Z","message":{"role":"assistant","content":" El"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.010996671Z","message":{"role":"assistant","content":" cielo"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.121965715Z","message":{"role":"assistant","content":" es"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.299675718Z","message":{"role":"assistant","content":" un"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.429267309Z","message":{"role":"assistant","content":" color"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.607947782Z","message":{"role":"assistant","content":" negro"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.721824475Z","message":{"role":"assistant","content":" y"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:07.899275938Z","message":{"role":"assistant","content":" azul"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.013422521Z","message":{"role":"assistant","content":" debido"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.194411494Z","message":{"role":"assistant","content":" al"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.311352126Z","message":{"role":"assistant","content":" re"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.506407367Z","message":{"role":"assistant","content":"frac"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.629716209Z","message":{"role":"assistant","content":"ción"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:08.901192158Z","message":{"role":"assistant","content":" y"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.017438371Z","message":{"role":"assistant","content":" la"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.206972862Z","message":{"role":"assistant","content":" absorción"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.399381534Z","message":{"role":"assistant","content":" de"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.515039496Z","message":{"role":"assistant","content":" la"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.696289069Z","message":{"role":"assistant","content":" luz"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:09.82081905Z","message":{"role":"assistant","content":" solar"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.011480392Z","message":{"role":"assistant","content":" por"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.194901744Z","message":{"role":"assistant","content":" las"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.308155347Z","message":{"role":"assistant","content":" moléculas"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.494352649Z","message":{"role":"assistant","content":" del"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.617334751Z","message":{"role":"assistant","content":" aire"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.795765214Z","message":{"role":"assistant","content":" y"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:10.995529414Z","message":{"role":"assistant","content":" el"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:11.197993284Z","message":{"role":"assistant","content":" espacio"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:11.313081816Z","message":{"role":"assistant","content":" interes"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:11.506970428Z","message":{"role":"assistant","content":"telar"},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:11.620706891Z","message":{"role":"assistant","content":"."},"done":false}
{"model":"gemma:2b","created_at":"2024-04-30T15:29:11.898162059Z","message":{"role":"assistant","content":""},"done":true,"total_duration":6877077389,"load_duration":1313820,"prompt_eval_duration":269637000,"eval_count":39,"eval_duration":6476435000}
```

### 6.6 Mediante consulta de la API REST con curl con parámetros (Modo Chat)

Consulta simple sin parámetros:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma:2b",
  "messages": [
    { "role": "user", "content": "¿porqué el cielo es azúl?" }
  ],
  "stream": false
}'
```

Ejemplo de salida

```bash
{"model":"gemma:2b","created_at":"2024-04-30T15:30:11.27210018Z","message":{"role":"assistant","content":"El cielo no es azúl. El cielo es un color azul debido a la refracción y la dispersión de la luz solar en los gases del espacio interestelar."},"done":true,"total_duration":2582132933,"load_duration":1024500,"prompt_eval_duration":117876000,"eval_count":35,"eval_duration":2321719000}
```
