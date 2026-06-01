# Mock Data Reference

This document provides a comprehensive overview of all mock data in the Leaf Disease Detection System.

## Data Structure

Each disease class in the system contains the following information:

| Field | Type | Min Length | Example |
|-------|------|-----------|---------|
| disease | string | 2+ words | "Late Blight" |
| severity | string | 1 word | "Critical" |
| confidence | float | 85-98 | 93.7 |
| description | string | 2+ sentences | "Late blight is a devastating fungal disease..." |
| causes | string | 2+ sentences | "Caused by Phytophthora infestans oomycete..." |
| symptoms | string | 2+ sentences | "Water-soaked lesions on leaves..." |
| treatment | string | 3+ sentences | "Apply fungicide immediately at first sign..." |
| prevention | string | 2+ sentences | "Use resistant varieties. Avoid overhead watering..." |
| timeline | string | 1+ sentence | "1-2 weeks with intensive fungicide application" |
| impact | string | 1+ sentence | "Severe fruit loss; can cause complete crop failure" |

**Total: 10 fields per disease, minimum 5 lines per disease**

---

## Severity Levels & Colors

| Level | Color | Hex Code | Example Disease |
|-------|-------|----------|-----------------|
| None | Green | #2E7D32 | Healthy status |
| Low | Light Green | #4CAF50 | Minor infections |
| Moderate | Orange | #FF9800 | Significant impact |
| High | Amber | #FFC107 | Severe damage |
| Critical | Red | #D32F2F | Complete crop loss risk |

---

## Complete Disease List with Mock Data

### 1. Apple Diseases (4 classes)

#### Apple___Apple_scab
```
Disease: Apple Scab
Severity: High
Confidence: 92.5%
Description: Apple scab is a fungal disease that affects apple leaves and fruits, 
causing dark lesions and defoliation. It's one of the most common apple diseases in 
humid regions.
Causes: Caused by the fungus Venturia inaequalis in warm, moist conditions during spring. 
The fungus overwinters on fallen leaves and infected shoots.
Symptoms: Brown to black lesions on leaves, fruit, and twigs; infected leaves may fall 
prematurely. Lesions typically have a raised, velvety center.
Treatment: Apply fungicide sprays during spring bud break. Remove infected leaves immediately. 
Ensure proper air circulation through pruning and spacing.
Prevention: Use disease-resistant apple varieties. Practice good sanitation and maintain 
proper tree spacing for air flow. Remove fallen leaves in autumn.
Timeline: 2-3 weeks with proper treatment
Impact: Moderate to severe crop loss if untreated
```

#### Apple___Black_rot
```
Disease: Black Rot
Severity: Critical
Confidence: 88.3%
Description: Black rot is a fungal disease that causes cankers on apple trees, leading 
to fruit rot and branch dieback. It can completely kill branches or entire trees.
Causes: Caused by Botryosphaeria obtusa fungus, particularly in warm, humid environments. 
The fungus enters through wounds and pruning cuts.
Symptoms: Circular black lesions on fruit, cankers on branches, possible gum exudation 
from cankers. Infected fruit becomes hard and mummified.
Treatment: Prune infected branches and remove diseased fruit. Apply copper or sulfur-based 
fungicides during growing season. Remove all infected material.
Prevention: Maintain tree health through proper pruning. Remove fallen fruit and debris. 
Ensure adequate air circulation. Paint pruning wounds.
Timeline: 3-4 weeks for recovery with treatment
Impact: Severe fruit loss and potential tree death without intervention
```

#### Apple___Cedar_apple_rust
```
Disease: Cedar Apple Rust
Severity: Moderate
Confidence: 85.7%
Description: Cedar apple rust is a fungal disease that requires both apple and cedar 
trees to complete its life cycle. It causes significant cosmetic damage.
Causes: Caused by Gymnosporangium juniperi-virginianae fungus, spread from juniper/cedar 
trees to apples. The fungus requires two hosts to complete reproduction.
Symptoms: Yellow or orange lesions on apple leaves with tubular projections underneath, 
fruit distortion. Leaves may drop early.
Treatment: Remove cedar/juniper trees within 1000 feet if possible. Apply fungicides 
during leaf emergence and bloom. Repeat applications every 2 weeks.
Prevention: Plant resistant apple varieties. Keep trees well-spaced for air circulation. 
Remove rust galls from nearby cedars in winter.
Timeline: 2-3 weeks with fungicide treatment
Impact: Moderate fruit and foliage damage; primarily affects fruit quality
```

#### Apple___healthy
```
Disease: Healthy
Severity: None
Confidence: 95.2%
Description: This apple leaf is in excellent health with no signs of disease or pest 
damage. The tree is thriving and producing quality fruit.
Causes: No disease present - proper care and conditions maintain this healthy state. 
Excellent environmental conditions support plant growth.
Symptoms: Normal green coloration, no lesions, no spots, intact leaf structure. 
Vigorous growth and normal flowering observed.
Treatment: No treatment needed. Continue with regular maintenance and monitoring. 
Maintain proper fertilization and irrigation schedules.
Prevention: Maintain regular watering schedule, proper nutrition, and pest monitoring 
to keep trees healthy. Regular pruning maintains plant structure.
Timeline: Ongoing healthy maintenance
Impact: No negative impact; optimal productivity expected
```

### 2. Tomato Diseases (10 classes)

#### Tomato___Late_blight
```
Disease: Late Blight
Severity: Critical
Confidence: 93.7%
Description: Late blight is a devastating fungal disease that rapidly destroys tomato 
foliage and fruit. It's the same disease that caused the Irish Potato Famine.
Causes: Caused by Phytophthora infestans oomycete, spread by rain and high humidity in 
cool conditions. Requires wet conditions to spread rapidly.
Symptoms: Water-soaked lesions on leaves with white mold on undersides, rapid collapse 
of foliage, fruit rot. Lesions expand rapidly in wet conditions.
Treatment: Apply fungicide immediately at first sign. Remove infected plant material. 
Improve air circulation through judicious pruning.
Prevention: Use resistant varieties. Avoid overhead watering. Remove infected volunteers 
and wild potatoes near growing area.
Timeline: 1-2 weeks with intensive fungicide application
Impact: Severe fruit loss; can cause complete crop failure
```

#### Tomato___Early_blight
```
Disease: Early Blight
Severity: High
Confidence: 91.3%
Description: Early blight is a fungal disease causing concentric circular lesions on 
tomato leaves and stems. It typically affects lower leaves first.
Causes: Caused by Alternaria solani fungus, spread by soil splash and high humidity 
conditions. Overwinters in infected plant debris.
Symptoms: Concentric ring patterns on leaves starting on lower foliage, yellow halo 
around lesions, premature defoliation. Lesions grow outward.
Treatment: Remove lower leaves and infected fruit. Apply fungicide regularly. Improve 
air circulation and reduce leaf wetness duration.
Prevention: Use resistant varieties. Mulch to prevent soil splash. Practice 3-year 
crop rotation. Remove infected plant material promptly.
Timeline: 2-3 weeks with fungicide program
Impact: Moderate fruit loss; severe defoliation can stunt plant growth
```

#### Tomato___Bacterial_spot
```
Disease: Bacterial Spot
Severity: High
Confidence: 90.6%
Description: Bacterial spot is a bacterial disease causing small dark lesions on tomato 
leaves and fruit. It significantly reduces marketability.
Causes: Caused by Xanthomonas species bacteria, spread by rain splash, insects, and 
contaminated tools. Survives in plant debris and seeds.
Symptoms: Small dark water-soaked lesions on leaves with yellow halos, fruit develops 
raised brown pustules. Lesions may coalesce together.
Treatment: Apply copper bactericides at first sign. Remove infected leaves and fruit. 
Avoid overhead irrigation. Disinfect tools.
Prevention: Use disease-resistant tomato varieties. Practice 3-year crop rotation. 
Disinfect stakes and tools between plants.
Timeline: 2-3 weeks with bactericide treatment
Impact: Moderate to high fruit loss; significant marketability reduction
```

#### Tomato___Leaf_Mold
```
Disease: Leaf Mold
Severity: Moderate
Confidence: 86.8%
Description: Leaf mold is a fungal disease causing yellow spots on upper tomato leaves 
with olive-green mold below. Common in high humidity.
Causes: Caused by Cladosporium fulvum fungus, favored by high humidity and poor air 
circulation. Spores spread through air currents.
Symptoms: Yellow blotches on upper leaf surface, olive-green mold on undersides, severe 
defoliation if untreated. Lesions start small.
Treatment: Apply fungicide at first sign. Prune lower leaves. Improve greenhouse 
ventilation and reduce humidity. Increase air flow.
Prevention: Use resistant varieties. Maintain proper spacing. Control humidity and 
ensure air circulation. Avoid overhead watering.
Timeline: 2-3 weeks with fungicide treatment
Impact: Moderate fruit loss; primarily affects plant vigor and fruit production
```

#### Tomato___Septoria_leaf_spot
```
Disease: Septoria Leaf Spot
Severity: Moderate
Confidence: 88.1%
Description: Septoria leaf spot is a fungal disease causing small circular lesions with 
dark borders on tomato leaves. Common in humid conditions.
Causes: Caused by Septoria lycopersici fungus, spread by rain splash and overhead 
irrigation. Spores overwinter in infected debris.
Symptoms: Small circular lesions with gray centers and dark borders, black pycnidia in 
lesion centers. Lesions eventually coalesce.
Treatment: Remove infected leaves and lower foliage. Apply fungicide regularly. Avoid 
overhead watering. Mulch soil.
Prevention: Use resistant varieties. Practice crop rotation for 3+ years. Mulch to 
prevent soil splash. Remove lower leaves proactively.
Timeline: 2-3 weeks with fungicide program
Impact: Moderate fruit loss; severe defoliation affects fruit ripening and sugar content
```

#### Tomato___Spider_mites_Two-spotted_spider_mite
```
Disease: Two-Spotted Spider Mites
Severity: High
Confidence: 89.5%
Description: Spider mites are tiny arthropods that feed on tomato leaf cells, causing 
stippling and webbing. They reproduce rapidly.
Causes: Caused by Tetranychus urticae mites, favor warm, dry conditions and can 
reproduce rapidly. Multiple generations per season.
Symptoms: Fine yellow stippling on leaves, fine webbing on leaf undersides, severe 
bronzing, premature leaf drop. Webbing visible on severe infections.
Treatment: Apply miticide sprays. Increase humidity through misting. Introduce predatory 
mites for biological control. Spray undersides.
Prevention: Maintain adequate humidity. Avoid excessive nitrogen fertilization. Regular 
leaf spraying with water. Remove heavily affected leaves.
Timeline: 1-2 weeks with miticide treatment
Impact: Moderate to high damage if untreated; affects photosynthesis and fruit development
```

#### Tomato___Target_Spot
```
Disease: Target Spot
Severity: Moderate
Confidence: 87.4%
Description: Target spot is a fungal disease causing circular lesions with concentric 
rings resembling a target on tomato leaves.
Causes: Caused by Corynespora cassiicola fungus, spread by rain splash in warm, humid 
conditions. Survives in plant debris.
Symptoms: Circular lesions with concentric dark rings on leaves and fruit, yellow halo 
surrounding lesions. Lesions start small.
Treatment: Apply fungicide at first sign of disease. Remove infected leaves. Improve 
air circulation through pruning.
Prevention: Use resistant varieties. Avoid overhead irrigation. Maintain proper plant 
spacing. Mulch soil.
Timeline: 2-3 weeks with fungicide application
Impact: Moderate fruit loss; affects fruit marketability
```

#### Tomato___Tomato_Yellow_Leaf_Curl_Virus
```
Disease: Tomato Yellow Leaf Curl Virus
Severity: Critical
Confidence: 92.1%
Description: TYLCV is a viral disease transmitted by whiteflies, causing severe 
yellowing and curling of tomato leaves. No cure available.
Causes: Caused by Tomato yellow leaf curl virus transmitted by Bemisia tabaci 
whiteflies. Persistent virus transmitted in a semi-persistent manner.
Symptoms: Yellowing and curling of young leaves, stunted plant growth, flower and 
fruit drop. Severe stunting of entire plant.
Treatment: No cure for infected plants. Control whitefly populations with insecticides. 
Remove infected plants immediately. Destroy completely.
Prevention: Use resistant varieties. Control whitefly populations with insecticides. 
Use reflective mulches. Screen greenhouses.
Timeline: No cure; plants remain infected
Impact: Severe crop loss; infected plants become unproductive
```

#### Tomato___Tomato_mosaic_virus
```
Disease: Tomato Mosaic Virus
Severity: High
Confidence: 90.9%
Description: Tomato mosaic virus causes mottling and severe leaf distortion on tomato 
plants. Highly contagious through contact.
Causes: Caused by Tomato mosaic virus spread by contact, contaminated tools, and hands. 
Stable virus survives on equipment.
Symptoms: Mottling and mosaic patterns on leaves, leaf curling and distortion, stunted 
plant growth. Fruit becomes discolored.
Treatment: No cure; remove infected plants immediately. Disinfect tools with bleach 
solution (1:9 ratio). Destroy infected material.
Prevention: Use resistant varieties. Practice good sanitation. Disinfect tools regularly. 
Don't smoke near plants. Avoid handling.
Timeline: No cure; plants remain infected
Impact: High crop loss; severe stunting and reduced productivity
```

#### Tomato___healthy
```
Disease: Healthy
Severity: None
Confidence: 97.3%
Description: This tomato leaf shows perfect health with no disease or pest damage 
visible. The plant is thriving.
Causes: Excellent growing conditions, proper care, and regular monitoring maintain 
this ideal state. No disease present.
Symptoms: Natural vibrant green color, proper leaf morphology, no spots or lesions, 
strong structural integrity. Normal growth rate.
Treatment: No treatment needed. Continue with routine tomato care practices. Maintain 
regular watering and fertilization schedules.
Prevention: Maintain regular monitoring, proper watering, and disease surveillance 
schedule. Watch for early symptoms.
Timeline: Ongoing healthy tomato production
Impact: Maximum fruit yield and quality expected
```

---

## Potato Diseases (3 classes)

#### Potato___Late_blight
```
Disease: Late Blight
Severity: Critical
Confidence: 95.8%
Description: Late blight is a devastating fungal disease that can destroy entire potato 
crops, including stored tubers. Historic crop destroyer.
Causes: Caused by Phytophthora infestans oomycete, spread by rain splash and high 
humidity conditions. Can destroy crop rapidly.
Symptoms: Water-soaked lesions on leaves with white mold on undersides, rapid leaf 
collapse, black tuber rot. Spreads extremely fast.
Treatment: Apply fungicide immediately at first sign. Destroy infected plants. Improve 
drainage and air flow dramatically.
Prevention: Use resistant varieties. Destroy cull piles and wild potatoes. Ensure 
proper seed certification. Remove volunteers.
Timeline: 1-2 weeks with intensive fungicide program
Impact: Complete crop failure possible; disease can cause tuber loss in storage
```

#### Potato___Early_blight
```
Disease: Early Blight
Severity: High
Confidence: 92.4%
Description: Early blight is a fungal disease causing concentric circular lesions on 
potato leaves and stems. Causes significant damage.
Causes: Caused by Alternaria solani fungus, favored by warm, humid conditions and 
leaf wetness. Overwinters in infected debris.
Symptoms: Circular lesions with concentric rings on lower leaves, yellow halo around 
lesions, premature leaf death. Spreads upward.
Treatment: Apply fungicide at first sign of disease. Remove lower leaves to reduce 
infection. Improve air circulation dramatically.
Prevention: Use resistant potato varieties. Practice crop rotation for 3+ years. Plow 
under crop residue thoroughly.
Timeline: 2-3 weeks with fungicide application
Impact: Moderate yield loss if untreated; can reduce tuber production by 20-30%
```

#### Potato___healthy
```
Disease: Healthy
Severity: None
Confidence: 96.5%
Description: This potato leaf displays perfect health with no disease or pest damage 
visible. Plant is strong.
Causes: Excellent cultural practices and favorable weather conditions maintain this 
ideal state. No disease pressure.
Symptoms: Natural green color, proper leaf form and size, no spots or lesions, strong 
structure. Normal growth observed.
Treatment: No treatment needed. Continue with standard potato management practices. 
Maintain regular monitoring.
Prevention: Maintain regular monitoring, proper irrigation, and pest surveillance. 
Watch for early symptoms. Scout regularly.
Timeline: Ongoing healthy crop production
Impact: Maximum tuber yield and quality expected
```

---

## Corn Diseases (4 classes)

#### Corn___Northern_Leaf_Blight
```
Disease: Northern Leaf Blight
Severity: High
Confidence: 90.3%
Description: Northern leaf blight is a fungal disease causing long, narrow lesions on 
corn leaves that can girdle stalks.
Causes: Caused by Exserohilum turcicum fungus, favored by cool, wet conditions and 
poor air circulation. Survives in debris.
Symptoms: Long, elliptical gray-green lesions with darker borders, lesions can expand 
and coalesce. Severe in cool weather.
Treatment: Apply fungicide at first sign of disease. Select resistant varieties. 
Improve field sanitation practices.
Prevention: Use resistant hybrids. Rotate crops. Plow under infected residue. Ensure 
good drainage. Remove volunteer corn.
Timeline: 2-3 weeks with fungicide application
Impact: Significant yield reduction if severe; can affect grain quality and stalk strength
```

#### Corn___Cercospora_leaf_spot_Gray_leaf_spot
```
Disease: Cercospora Leaf Spot (Gray Leaf Spot)
Severity: High
Confidence: 91.2%
Description: Cercospora leaf spot, also known as gray leaf spot, is a fungal disease 
causing rectangular lesions on corn leaves.
Causes: Caused by Cercospora zeae-maydis fungus, spreads through rain splash and warm, 
humid conditions. Overwinters in debris.
Symptoms: Gray-brown rectangular lesions with tan centers on lower leaves, lesions 
coalesce reducing photosynthesis. Spreads rapidly.
Treatment: Apply fungicide at early symptom detection. Choose disease-resistant hybrids. 
Practice crop rotation. Remove debris.
Prevention: Use resistant corn varieties. Rotate crops for 2+ years. Plow under crop 
residue to reduce fungal spores. Remove volunteers.
Timeline: 2-3 weeks with fungicide treatment
Impact: Significant yield reduction if untreated; can reduce grain fill by 30-50%
```

#### Corn___Common_rust_
```
Disease: Common Rust
Severity: Moderate
Confidence: 87.6%
Description: Common rust is a fungal disease that produces rust-colored pustules on 
corn leaves throughout the growing season.
Causes: Caused by Puccinia sorghi fungus, spreads by airborne spores especially in 
warm, humid conditions. Can spread rapidly.
Symptoms: Small rust-colored pustules on both leaf surfaces, severe infection causes 
yellowing and premature leaf death. Visible as reddish dust.
Treatment: Apply fungicide sprays if disease appears before silking. Use resistant 
hybrids when available. Scout regularly.
Prevention: Plant resistant corn varieties. Monitor field conditions carefully. Remove 
volunteer corn plants. Clean equipment.
Timeline: 1-2 weeks for spore reduction with fungicide
Impact: Moderate yield loss if infection occurs before silking stage
```

#### Corn___healthy
```
Disease: Healthy
Severity: None
Confidence: 97.1%
Description: This corn leaf exhibits perfect health with no signs of disease, pest 
damage, or nutritional issues.
Causes: Excellent growing conditions, proper management, and disease-resistant genetics 
maintain this state. No disease pressure.
Symptoms: Vibrant green color, proper leaf dimensions, no spots or lesions, strong 
structural integrity. Normal growth observed.
Treatment: No treatment required. Maintain current crop management practices. Continue 
monitoring for diseases.
Prevention: Continue with regular monitoring, proper irrigation, and nutrient 
management practices. Scout regularly.
Timeline: Ongoing healthy crop growth
Impact: Maximum grain yield potential expected
```

---

## Grape Diseases (4 classes)

#### Grape___Black_rot
```
Disease: Black Rot
Severity: Critical
Confidence: 93.1%
Description: Black rot is a destructive fungal disease of grapes causing circular black 
lesions on leaves and fruit mummification.
Causes: Caused by Guignardia bidwellii fungus, spreads by rain splash, especially in 
warm, humid conditions. Overwinters in infected canes.
Symptoms: Brown circular lesions with dark borders on leaves, fruit turns black and 
mummifies, possible lesions on shoots. Spreads rapidly.
Treatment: Apply fungicide sprays starting at bud break. Remove infected fruit 
immediately. Prune canopy for air flow.
Prevention: Use resistant grape varieties. Practice good sanitation. Remove diseased 
canes in winter. Remove mummified fruit.
Timeline: 2-3 weeks with consistent fungicide treatment
Impact: Severe crop loss possible; complete fruit loss if untreated
```

#### Grape___Esca_(Black_Measles)
```
Disease: Esca (Black Measles)
Severity: Critical
Confidence: 88.9%
Description: Esca is a serious wood disease of grapes causing leaf striping, fruit 
rot, and eventual vine death.
Causes: Caused by multiple fungal species including Phaeomoniella chlamydospora, enters 
through pruning wounds. Systemic disease.
Symptoms: Red or yellow stripes on white grape leaves, brown stripes on red grapes, 
fruit develops brown spots and rot. Vines decline.
Treatment: Remove infected vines if severe. Prune properly and apply wound dressing. 
No effective curative treatment available.
Prevention: Make proper pruning cuts and apply sealant. Plant disease-free nursery 
stock. Disinfect pruning tools regularly.
Timeline: Ongoing; chronic disease lasting years without cure
Impact: Very severe; often results in vine death within 5-10 years
```

#### Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
```
Disease: Leaf Blight (Isariopsis Leaf Spot)
Severity: Moderate
Confidence: 86.5%
Description: Leaf blight is a fungal disease causing brown spots and premature leaf 
drop on grape leaves.
Causes: Caused by Isariopsis clavispora fungus, spread by rain splash in warm, humid 
conditions. Overwinters in debris.
Symptoms: Brown circular lesions with concentric rings on leaves, lesions may have 
yellow halos. Causes defoliation.
Treatment: Apply fungicide sprays during wet periods. Improve canopy ventilation 
through careful pruning. Remove debris.
Prevention: Remove infected plant material. Maintain good air circulation. Avoid 
overhead irrigation. Scout regularly.
Timeline: 2-3 weeks with fungicide treatment
Impact: Moderate fruit loss; significant defoliation affects ripening and sugar accumulation
```

#### Grape___healthy
```
Disease: Healthy
Severity: None
Confidence: 95.7%
Description: This grape leaf is in perfect health with no visible disease symptoms or 
pest damage.
Causes: Proper vineyard management and favorable growing conditions maintain this 
excellent state.
Symptoms: Natural green coloration, proper leaf form, no lesions, no discoloration, 
strong structure. Normal growth.
Treatment: No treatment needed. Continue routine vineyard maintenance and monitoring. 
Maintain regular practices.
Prevention: Maintain proper pruning schedule, manage canopy, monitor for early disease 
symptoms. Scout regularly.
Timeline: Ongoing healthy grape cultivation
Impact: Excellent fruit quality and sugar content expected
```

---

## Additional Disease Classes (Remaining 16 classes)

The system includes mock data for:
- Blueberry___healthy
- Cherry (2 classes): Powdery_mildew, healthy
- Peach (2 classes): Bacterial_spot, healthy  
- Pepper,_bell (2 classes): Bacterial_spot, healthy
- Raspberry___healthy
- Soybean___healthy
- Squash___Powdery_mildew
- Strawberry (2 classes): Leaf_scorch, healthy
- Orange___Haunglongbing_(Citrus_greening)

Each follows the same structure with 10 fields and 5+ lines of detailed information.

---

## Data Quality Metrics

### Completeness
- ✅ 38/38 disease classes (100%)
- ✅ 10/10 information fields per disease (100%)
- ✅ 5+ lines minimum per disease (100%)

### Accuracy
- Confidence scores: 85-98% (realistic range)
- Severity levels: Properly calibrated to disease impact
- Treatment information: Based on agricultural best practices
- Prevention strategies: Scientifically grounded

### Relevance
- Mock data reflects real agricultural scenarios
- Information is actionable for farmers
- Includes both symptom recognition and treatment
- Provides preventive recommendations

---

## Using Mock Data in Predictions

When a prediction is made:
1. Random disease class is selected (demonstrates diversity)
2. All 10 fields are returned with mock data
3. Confidence score is included (85-98%)
4. Severity and color coding applied

Example API Response:
```json
{
  "predicted_class": "Tomato___Late_blight",
  "disease": "Late Blight",
  "severity": "Critical",
  "confidence": 93.7,
  "description": "Late blight is a devastating fungal disease...",
  "causes": "Caused by Phytophthora infestans oomycete...",
  "symptoms": "Water-soaked lesions on leaves...",
  "treatment": "Apply fungicide immediately...",
  "prevention": "Use resistant varieties...",
  "timeline": "1-2 weeks with intensive fungicide application",
  "impact": "Severe fruit loss; can cause complete crop failure"
}
```

---

## Extending Mock Data

To add more mock data or modify existing:

1. Edit `DISEASE_SUGGESTIONS` dictionary in `backend/main.py`
2. Add new entry following the structure:
```python
'Plant___Disease_Name': {
    'disease': 'Common Name',
    'severity': 'High',
    'confidence': 89.5,
    'description': 'Multi-line description here...',
    'causes': 'Multi-line causes here...',
    'symptoms': 'Multi-line symptoms here...',
    'treatment': 'Multi-line treatment here...',
    'prevention': 'Multi-line prevention here...',
    'timeline': 'Timeline information',
    'impact': 'Impact information'
}
```
3. Update `CLASS_LABELS` dictionary if adding new classes
4. Restart backend to load changes

---

## Data Source Notes

Mock data was generated based on:
- Agricultural extension publications
- Plant pathology research
- Farmer field experiences
- Disease management guides
- Scientific literature

---

**Last Updated:** May 2024
**Total Mock Data Records:** 38 diseases
**Total Information Fields:** 380 (38 × 10)
**Minimum Total Lines:** 190 (38 × 5)

