DIR="/home/ec2-user/datos"
FILE="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
BUCKET="mi-bucket-devops-alexbaezcas"
LOG="backup.log"

echo "Inicio $(date)" >> $LOG

# Validar que el directorio exista
if [ ! -d "$DIR" ]; then
  echo "Error: el directorio no existe" >> $LOG
  exit 1
fi

# Comprimir
tar -czf $FILE $DIR

if [ $? -ne 0 ]; then
  echo "Error al comprimir" >> $LOG
  exit 1
fi

# Subir a S3
aws s3 cp $FILE s3://$BUCKET/

if [ $? -ne 0 ]; then
  echo "Error al subir a S3" >> $LOG
  exit 1
fi

echo "Backup completado correctamente $(date)" >> $LOG