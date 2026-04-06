import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

def listar_instancias():
    try:
        response = ec2.describe_instances()
        for r in response['Reservations']:
            for i in r['Instances']:
                print(f"ID: {i['InstanceId']} - Estado: {i['State']['Name']}")
    except Exception as e:
        print("Error al listar instancias:", e)

def gestionar_instancia(instancia_id, accion):
    try:
        if accion == "iniciar":
            ec2.start_instances(InstanceIds=[instancia_id])
            print(f"Instancia {instancia_id} iniciándose...")
        elif accion == "detener":
            ec2.stop_instances(InstanceIds=[instancia_id])
            print(f"Instancia {instancia_id} deteniéndose...")
        else:
            print("Acción no válida")
    except Exception as e:
        print("Error:", e)

# --- MENÚ ---
while True:
    print("\n--- MENÚ EC2 ---")
    print("1. Listar instancias")
    print("2. Iniciar instancia")
    print("3. Detener instancia")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        listar_instancias()

    elif opcion == "2":
        instancia_id = input("ID de la instancia: ")
        gestionar_instancia(instancia_id, "iniciar")

    elif opcion == "3":
        instancia_id = input("ID de la instancia: ")
        gestionar_instancia(instancia_id, "detener")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
