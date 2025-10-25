import openai
from django.conf import settings
import json


def generate_mitigation_recommendations(
    risk_title, risk_description, likelihood, impact
):
    """
    Genera recomendaciones de mitigación usando OpenAI v2.6.1
    """
    print("🔍 Usando OpenAI v2.6.1")

    # ✅ CONFIGURACIÓN CORRECTA para v2.6.1
    client = openai.OpenAI(
        api_key=settings.OPENAI_API_KEY,
        # La v2.6.1 maneja proxies automáticamente, no necesitas configurarlos
    )

    risk_level = likelihood * impact
    risk_level_name = (
        "Crítico"
        if risk_level > 20
        else "Alto"
        if risk_level > 12
        else "Medio"
        if risk_level > 5
        else "Bajo"
    )

    prompt = f"""Eres un experto en gestión de riesgos de seguridad para empresas ISP.

RIESGO:
- Título: {risk_title}
- Descripción: {risk_description}
- Probabilidad: {likelihood}/5
- Impacto: {impact}/5
- Nivel de Riesgo: {risk_level_name}

Proporciona 3 acciones de mitigación en formato JSON:

{{
  "recommendations": [
    {{
      "action": "nombre acción 1",
      "due_days": 30,
      "priority": "alta"
    }},
    {{
      "action": "nombre acción 2", 
      "due_days": 60,
      "priority": "media"
    }},
    {{
      "action": "nombre acción 3",
      "due_days": 90,
      "priority": "baja"
    }}
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.7,
        )

        response_text = response.choices[0].message.content.strip()
        response_text = response_text.replace("```json", "").replace("```", "").strip()

        print(f"✅ Respuesta recibida: {response_text[:100]}...")
        return json.loads(response_text)

    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            "recommendations": [
                {
                    "action": "Revisar y documentar el riesgo manualmente",
                    "due_days": 30,
                    "priority": "alta",
                }
            ]
        }
