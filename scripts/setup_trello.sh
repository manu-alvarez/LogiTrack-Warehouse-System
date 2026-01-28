#!/bin/bash
# LogiTrack - Trello Board Setup Script
# This script creates the Trello board, lists, and sample cards

# Configuration - Replace with your actual credentials
TRELLO_API_KEY="${TRELLO_API_KEY:-YOUR_API_KEY}"
TRELLO_TOKEN="${TRELLO_TOKEN:-YOUR_TOKEN}"
BASE_URL="https://api.trello.com/1"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== LogiTrack - Trello Board Setup ===${NC}"

# Check if credentials are set
if [[ "$TRELLO_API_KEY" == "YOUR_API_KEY" ]] || [[ "$TRELLO_TOKEN" == "YOUR_TOKEN" ]]; then
    echo "⚠️  Please set your Trello credentials:"
    echo "   export TRELLO_API_KEY='your_api_key'"
    echo "   export TRELLO_TOKEN='your_token'"
    echo ""
    echo "Get your API key at: https://trello.com/1/appKey/generate"
    exit 1
fi

# Create Board
echo -e "\n${GREEN}Creating board...${NC}"
BOARD_RESPONSE=$(curl -s -X POST "${BASE_URL}/boards" \
  -d "name=LogiTrack - Operaciones de Almacén" \
  -d "defaultLists=false" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}")

BOARD_ID=$(echo $BOARD_RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

if [[ -z "$BOARD_ID" ]]; then
    echo "❌ Error creating board. Response:"
    echo $BOARD_RESPONSE
    exit 1
fi
echo "✅ Board created: $BOARD_ID"

# Create Lists (in reverse order so they appear correctly)
echo -e "\n${GREEN}Creating lists...${NC}"

LISTS=(
    "⚠️ Incidencias / Parados"
    "🚚 Enviados / Salida"
    "🏷️ Etiquetado y Listo"
    "📦 Embalaje y Packing"
    "🛠️ En Preparación"
    "🔥 PRIORIDAD (Salida Hoy)"
    "📥 Pedidos por Entrar"
)

declare -A LIST_IDS

for list_name in "${LISTS[@]}"; do
    RESPONSE=$(curl -s -X POST "${BASE_URL}/boards/${BOARD_ID}/lists" \
      -d "name=${list_name}" \
      -d "key=${TRELLO_API_KEY}" \
      -d "token=${TRELLO_TOKEN}")
    
    LIST_ID=$(echo $RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
    LIST_IDS["$list_name"]=$LIST_ID
    echo "✅ List created: $list_name"
done

# Get Red label ID
echo -e "\n${GREEN}Getting labels...${NC}"
LABELS_RESPONSE=$(curl -s -X GET "${BASE_URL}/boards/${BOARD_ID}/labels?key=${TRELLO_API_KEY}&token=${TRELLO_TOKEN}")
RED_LABEL_ID=$(echo $LABELS_RESPONSE | grep -o '"id":"[^"]*","idBoard":"[^"]*","name":"[^"]*","color":"red"' | head -1 | cut -d'"' -f4)

# Create Cards
echo -e "\n${GREEN}Creating sample cards...${NC}"

# Card 1: Pedido #501 - Cliente S.A. (Prioridad, Red label)
PRIORIDAD_LIST_ID="${LIST_IDS["🔥 PRIORIDAD (Salida Hoy)"]}"
CARD1_RESPONSE=$(curl -s -X POST "${BASE_URL}/cards" \
  -d "idList=${PRIORIDAD_LIST_ID}" \
  -d "name=Pedido #501 - Cliente S.A." \
  -d "desc=Pedido urgente de Cliente S.A. - Prioridad máxima para salida hoy." \
  -d "idLabels=${RED_LABEL_ID}" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}")
echo "✅ Card created: Pedido #501 - Cliente S.A. (PRIORIDAD)"

# Card 2: Pedido #502 - Local S.L. (En Preparación, with checklist)
PREPARACION_LIST_ID="${LIST_IDS["🛠️ En Preparación"]}"
CARD2_RESPONSE=$(curl -s -X POST "${BASE_URL}/cards" \
  -d "idList=${PREPARACION_LIST_ID}" \
  -d "name=Pedido #502 - Local S.L." \
  -d "desc=Pedido estándar de Local S.L." \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}")

CARD2_ID=$(echo $CARD2_RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

# Add checklist to Card 2
CHECKLIST_RESPONSE=$(curl -s -X POST "${BASE_URL}/cards/${CARD2_ID}/checklists" \
  -d "name=Productos" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}")

CHECKLIST_ID=$(echo $CHECKLIST_RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

# Add items to checklist
curl -s -X POST "${BASE_URL}/checklists/${CHECKLIST_ID}/checkItems" \
  -d "name=Producto A - 10 unidades" \
  -d "checked=true" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}" > /dev/null

curl -s -X POST "${BASE_URL}/checklists/${CHECKLIST_ID}/checkItems" \
  -d "name=Producto B - 5 unidades" \
  -d "checked=false" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}" > /dev/null

curl -s -X POST "${BASE_URL}/checklists/${CHECKLIST_ID}/checkItems" \
  -d "name=Producto C - 20 unidades" \
  -d "checked=false" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}" > /dev/null

echo "✅ Card created: Pedido #502 - Local S.L. (En Preparación + Checklist)"

# Card 3: Pedido #503 - Distribución Norte (Incidencias, with comment)
INCIDENCIAS_LIST_ID="${LIST_IDS["⚠️ Incidencias / Parados"]}"
CARD3_RESPONSE=$(curl -s -X POST "${BASE_URL}/cards" \
  -d "idList=${INCIDENCIAS_LIST_ID}" \
  -d "name=Pedido #503 - Distribución Norte" \
  -d "desc=Pedido con incidencia - revisar comentarios." \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}")

CARD3_ID=$(echo $CARD3_RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

# Add comment to Card 3
curl -s -X POST "${BASE_URL}/cards/${CARD3_ID}/actions/comments" \
  -d "text=Falta stock tornillería M8" \
  -d "key=${TRELLO_API_KEY}" \
  -d "token=${TRELLO_TOKEN}" > /dev/null

echo "✅ Card created: Pedido #503 - Distribución Norte (Incidencias + Comentario)"

# Get board URL
BOARD_URL="https://trello.com/b/${BOARD_ID}"
echo -e "\n${BLUE}=== Setup Complete ===${NC}"
echo "🎉 Board URL: ${BOARD_URL}"
echo ""
echo "Board ID: ${BOARD_ID}"
