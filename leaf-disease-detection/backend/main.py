from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg19 import preprocess_input
from PIL import Image
import numpy as np
import io
import uvicorn
# Initialize FastAPI application
app = FastAPI(title="Leaf Disease Detection System", version="1.0.0")

MODEL_PATH = "model/best_model.h5"
model = load_model(MODEL_PATH)
print("Model Input Shape:", model.input_shape)
print("Model Output Shape:", model.output_shape)

IMG_SIZE = (256, 256)  # use training image size

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Class mapping for 38 plant disease classes
CLASS_LABELS = {
    0: 'Apple___Apple_scab',
    1: 'Apple___Black_rot',
    2: 'Apple___Cedar_apple_rust',
    3: 'Apple___healthy',
    4: 'Blueberry___healthy',
    5: 'Cherry_(including_sour)___Powdery_mildew',
    6: 'Cherry_(including_sour)___healthy',
    7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    8: 'Corn_(maize)___Common_rust_',
    9: 'Corn_(maize)___Northern_Leaf_Blight',
    10: 'Corn_(maize)___healthy',
    11: 'Grape___Black_rot',
    12: 'Grape___Esca_(Black_Measles)',
    13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    14: 'Grape___healthy',
    15: 'Orange___Haunglongbing_(Citrus_greening)',
    16: 'Peach___Bacterial_spot',
    17: 'Peach___healthy',
    18: 'Pepper,_bell___Bacterial_spot',
    19: 'Pepper,_bell___healthy',
    20: 'Potato___Early_blight',
    21: 'Potato___Late_blight',
    22: 'Potato___healthy',
    23: 'Raspberry___healthy',
    24: 'Soybean___healthy',
    25: 'Squash___Powdery_mildew',
    26: 'Strawberry___Leaf_scorch',
    27: 'Strawberry___healthy',
    28: 'Tomato___Bacterial_spot',
    29: 'Tomato___Early_blight',
    30: 'Tomato___Late_blight',
    31: 'Tomato___Leaf_Mold',
    32: 'Tomato___Septoria_leaf_spot',
    33: 'Tomato___Spider_mites Two-spotted_spider_mite',
    34: 'Tomato___Target_Spot',
    35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    36: 'Tomato___Tomato_mosaic_virus',
    37: 'Tomato___healthy'
}

# Mock suggestion data for all 38 classes
DISEASE_SUGGESTIONS = {
    'Apple___Apple_scab': {
        'disease': 'Apple Scab',
        'severity': 'High',
        'confidence': 92.5,
        'description': 'Apple scab is a fungal disease that affects apple leaves and fruits, causing dark lesions and defoliation.',
        'causes': 'Caused by the fungus Venturia inaequalis in warm, moist conditions during spring.',
        'symptoms': 'Brown to black lesions on leaves, fruit, and twigs; infected leaves may fall prematurely.',
        'treatment': 'Apply fungicide sprays during spring bud break. Remove infected leaves immediately. Ensure proper air circulation.',
        'prevention': 'Use disease-resistant apple varieties. Practice good sanitation and maintain proper tree spacing for air flow.',
        'timeline': '2-3 weeks with proper treatment',
        'impact': 'Moderate to severe crop loss if untreated'
    },
    'Apple___Black_rot': {
        'disease': 'Black Rot',
        'severity': 'Critical',
        'confidence': 88.3,
        'description': 'Black rot is a fungal disease that causes cankers on apple trees, leading to fruit rot and branch dieback.',
        'causes': 'Caused by Botryosphaeria obtusa fungus, particularly in warm, humid environments.',
        'symptoms': 'Circular black lesions on fruit, cankers on branches, possible gum exudation from cankers.',
        'treatment': 'Prune infected branches and remove diseased fruit. Apply copper or sulfur-based fungicides during growing season.',
        'prevention': 'Maintain tree health through proper pruning. Remove fallen fruit and debris. Ensure adequate air circulation.',
        'timeline': '3-4 weeks for recovery with treatment',
        'impact': 'Severe fruit loss and potential tree death without intervention'
    },
    'Apple___Cedar_apple_rust': {
        'disease': 'Cedar Apple Rust',
        'severity': 'Moderate',
        'confidence': 85.7,
        'description': 'Cedar apple rust is a fungal disease that requires both apple and cedar trees to complete its life cycle.',
        'causes': 'Caused by Gymnosporangium juniperi-virginianae fungus, spread from juniper/cedar trees to apples.',
        'symptoms': 'Yellow or orange lesions on apple leaves with tubular projections underneath, fruit distortion.',
        'treatment': 'Remove cedar/juniper trees within 1000 feet if possible. Apply fungicides during leaf emergence and bloom.',
        'prevention': 'Plant resistant apple varieties. Keep trees well-spaced for air circulation. Remove rust galls from nearby cedars.',
        'timeline': '2-3 weeks with fungicide treatment',
        'impact': 'Moderate fruit and foliage damage; primarily affects fruit quality'
    },
    'Apple___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 95.2,
        'description': 'This apple leaf is in excellent health with no signs of disease or pest damage.',
        'causes': 'No disease present - proper care and conditions maintain this healthy state.',
        'symptoms': 'Normal green coloration, no lesions, no spots, intact leaf structure.',
        'treatment': 'No treatment needed. Continue with regular maintenance and monitoring.',
        'prevention': 'Maintain regular watering schedule, proper nutrition, and pest monitoring to keep trees healthy.',
        'timeline': 'Ongoing healthy maintenance',
        'impact': 'No negative impact; optimal productivity expected'
    },
    'Blueberry___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 96.1,
        'description': 'This blueberry leaf shows no signs of disease, pests, or nutritional deficiencies.',
        'causes': 'No disease present - excellent growing conditions and care maintain this state.',
        'symptoms': 'Natural green color, proper leaf size, no discoloration, no visible damage.',
        'treatment': 'No treatment required. Maintain current care practices.',
        'prevention': 'Continue with proper irrigation, mulching, and regular monitoring for pests and diseases.',
        'timeline': 'Ongoing healthy cultivation',
        'impact': 'Excellent berry production expected'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'disease': 'Powdery Mildew',
        'severity': 'Moderate',
        'confidence': 89.4,
        'description': 'Powdery mildew is a fungal disease that creates a white powder coating on leaves, flowers, and fruits.',
        'causes': 'Caused by Podosphaera celandii fungus, favored by warm days and cool nights with high humidity.',
        'symptoms': 'White powdery coating on leaves and fruit, leaf curling, premature leaf drop, distorted growth.',
        'treatment': 'Apply sulfur dust or fungicide sprays weekly. Remove heavily infected leaves. Improve air circulation.',
        'prevention': 'Maintain proper spacing between trees. Avoid excessive nitrogen fertilization. Use resistant cherry varieties.',
        'timeline': '1-2 weeks with regular fungicide application',
        'impact': 'Moderate to high fruit loss; primarily affects fruit quality and marketability'
    },
    'Cherry_(including_sour)___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 94.8,
        'description': 'This cherry leaf is completely healthy with no disease or pest damage visible.',
        'causes': 'Optimal growing conditions and good cultural practices maintain this healthy state.',
        'symptoms': 'Normal coloration, proper morphology, no lesions or spots, strong leaf structure.',
        'treatment': 'No treatment needed. Continue with routine orchard maintenance.',
        'prevention': 'Maintain consistent watering, provide proper nutrients, monitor for early signs of disease.',
        'timeline': 'Ongoing health maintenance',
        'impact': 'High-quality fruit production expected'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'disease': 'Cercospora Leaf Spot (Gray Leaf Spot)',
        'severity': 'High',
        'confidence': 91.2,
        'description': 'Cercospora leaf spot, also known as gray leaf spot, is a fungal disease causing rectangular lesions on corn leaves.',
        'causes': 'Caused by Cercospora zeae-maydis fungus, spreads through rain splash and warm, humid conditions.',
        'symptoms': 'Gray-brown rectangular lesions with tan centers on lower leaves, lesions coalesce reducing photosynthesis.',
        'treatment': 'Apply fungicide at early symptom detection. Choose disease-resistant hybrids. Practice crop rotation.',
        'prevention': 'Use resistant corn varieties. Rotate crops for 2+ years. Plow under crop residue to reduce fungal spores.',
        'timeline': '2-3 weeks with fungicide treatment',
        'impact': 'Significant yield reduction if untreated; can reduce grain fill by 30-50%'
    },
    'Corn_(maize)___Common_rust_': {
        'disease': 'Common Rust',
        'severity': 'Moderate',
        'confidence': 87.6,
        'description': 'Common rust is a fungal disease that produces rust-colored pustules on corn leaves throughout the growing season.',
        'causes': 'Caused by Puccinia sorghi fungus, spreads by airborne spores especially in warm, humid conditions.',
        'symptoms': 'Small rust-colored pustules on both leaf surfaces, severe infection causes yellowing and premature leaf death.',
        'treatment': 'Apply fungicide sprays if disease appears before silking. Use resistant hybrids when available.',
        'prevention': 'Plant resistant corn varieties. Monitor field conditions. Remove volunteer corn plants.',
        'timeline': '1-2 weeks for spore reduction with fungicide',
        'impact': 'Moderate yield loss if infection occurs before silking stage'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'disease': 'Northern Leaf Blight',
        'severity': 'High',
        'confidence': 90.3,
        'description': 'Northern leaf blight is a fungal disease causing long, narrow lesions on corn leaves that can girdle stalks.',
        'causes': 'Caused by Exserohilum turcicum fungus, favored by cool, wet conditions and poor air circulation.',
        'symptoms': 'Long, elliptical gray-green lesions with darker borders, lesions can expand and coalesce.',
        'treatment': 'Apply fungicide at first sign of disease. Select resistant varieties. Improve field sanitation.',
        'prevention': 'Use resistant hybrids. Rotate crops. Plow under infected residue. Ensure good drainage.',
        'timeline': '2-3 weeks with fungicide application',
        'impact': 'Significant yield reduction if severe; can affect grain quality and stalk strength'
    },
    'Corn_(maize)___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 97.1,
        'description': 'This corn leaf exhibits perfect health with no signs of disease, pest damage, or nutritional issues.',
        'causes': 'Excellent growing conditions, proper management, and disease-resistant genetics maintain this state.',
        'symptoms': 'Vibrant green color, proper leaf dimensions, no spots or lesions, strong structural integrity.',
        'treatment': 'No treatment required. Maintain current crop management practices.',
        'prevention': 'Continue with regular monitoring, proper irrigation, and nutrient management.',
        'timeline': 'Ongoing healthy crop growth',
        'impact': 'Maximum grain yield potential expected'
    },
    'Grape___Black_rot': {
        'disease': 'Black Rot',
        'severity': 'Critical',
        'confidence': 93.1,
        'description': 'Black rot is a destructive fungal disease of grapes causing circular black lesions on leaves and fruit mummification.',
        'causes': 'Caused by Guignardia bidwellii fungus, spreads by rain splash, especially in warm, humid conditions.',
        'symptoms': 'Brown circular lesions with dark borders on leaves, fruit turns black and mummifies, possible lesions on shoots.',
        'treatment': 'Apply fungicide sprays starting at bud break. Remove infected fruit immediately. Prune canopy for air flow.',
        'prevention': 'Use resistant grape varieties. Practice good sanitation and Remove diseased canes in winter.',
        'timeline': '2-3 weeks with consistent fungicide treatment',
        'impact': 'Severe crop loss possible; complete fruit loss if untreated'
    },
    'Grape___Esca_(Black_Measles)': {
        'disease': 'Esca (Black Measles)',
        'severity': 'Critical',
        'confidence': 88.9,
        'description': 'Esca is a serious wood disease of grapes causing leaf striping, fruit rot, and eventual vine death.',
        'causes': 'Caused by multiple fungal species including Phaeomoniella chlamydospora, enters through pruning wounds.',
        'symptoms': 'Red or yellow stripes on white grape leaves, brown stripes on red grapes, fruit develops brown spots and rot.',
        'treatment': 'Remove infected vines if severe. Prune properly and apply wound dressing. No effective curative treatment.',
        'prevention': 'Make proper pruning cuts and apply sealant. Plant disease-free nursery stock. Disinfect pruning tools.',
        'timeline': 'Ongoing; chronic disease lasting years without cure',
        'impact': 'Very severe; often results in vine death within 5-10 years'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'disease': 'Leaf Blight (Isariopsis Leaf Spot)',
        'severity': 'Moderate',
        'confidence': 86.5,
        'description': 'Leaf blight is a fungal disease causing brown spots and premature leaf drop on grape leaves.',
        'causes': 'Caused by Isariopsis clavispora fungus, spread by rain splash in warm, humid conditions.',
        'symptoms': 'Brown circular lesions with concentric rings on leaves, lesions may have yellow halos.',
        'treatment': 'Apply fungicide sprays during wet periods. Improve canopy ventilation through careful pruning.',
        'prevention': 'Remove infected plant material. Maintain good air circulation. Avoid overhead irrigation.',
        'timeline': '2-3 weeks with fungicide treatment',
        'impact': 'Moderate fruit loss; significant defoliation affects ripening and sugar accumulation'
    },
    'Grape___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 95.7,
        'description': 'This grape leaf is in perfect health with no visible disease symptoms or pest damage.',
        'causes': 'Proper vineyard management and favorable growing conditions maintain this excellent state.',
        'symptoms': 'Natural green coloration, proper leaf form, no lesions, no discoloration, strong structure.',
        'treatment': 'No treatment needed. Continue routine vineyard maintenance and monitoring.',
        'prevention': 'Maintain proper pruning schedule, manage canopy, monitor for early disease symptoms.',
        'timeline': 'Ongoing healthy grape cultivation',
        'impact': 'Excellent fruit quality and sugar content expected'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'disease': 'Huanglongbing (Citrus Greening)',
        'severity': 'Critical',
        'confidence': 94.2,
        'description': 'Huanglongbing (HLB), also called citrus greening, is a devastating bacterial disease affecting all citrus trees.',
        'causes': 'Caused by Candidatus Liberibacter bacteria transmitted by Asian citrus psyllid insects.',
        'symptoms': 'Mottled yellow leaves with asymmetrical patterns, small fruit, bitter taste, poor development.',
        'treatment': 'Difficult to treat; remove infected trees. Control psyllid populations with insecticides.',
        'prevention': 'Control psyllid populations. Use certified disease-free nursery trees. Quarantine infected areas.',
        'timeline': 'No cure; trees decline gradually over 5+ years',
        'impact': 'Fatal disease; trees eventually die; complete economic loss'
    },
    'Peach___Bacterial_spot': {
        'disease': 'Bacterial Spot',
        'severity': 'Moderate',
        'confidence': 87.3,
        'description': 'Bacterial spot is a bacterial disease causing dark lesions on peach leaves, fruit, and twigs.',
        'causes': 'Caused by Xanthomonas arboricola pv. pruni bacteria, spread by rain splash and insect activity.',
        'symptoms': 'Small dark water-soaked lesions on leaves with yellow halos, lesions coalesce causing shot-hole effect.',
        'treatment': 'Apply copper-based bactericides during growing season. Prune infected branches. Remove infected fruit.',
        'prevention': 'Use resistant peach varieties. Practice good sanitation. Ensure proper tree spacing for air flow.',
        'timeline': '2-3 weeks for symptom reduction with bactericide',
        'impact': 'Moderate fruit damage; cosmetic damage reduces market value'
    },
    'Peach___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 93.6,
        'description': 'This peach leaf shows no disease or pest damage and exhibits optimal health characteristics.',
        'causes': 'Excellent orchard management and favorable growing conditions support this healthy state.',
        'symptoms': 'Natural green color, proper leaf size and form, no lesions or spots, intact structure.',
        'treatment': 'No treatment required. Maintain routine orchard practices.',
        'prevention': 'Continue with regular monitoring, watering, and pest management.',
        'timeline': 'Ongoing healthy tree maintenance',
        'impact': 'High fruit quality and yield expected'
    },
    'Pepper,_bell___Bacterial_spot': {
        'disease': 'Bacterial Spot',
        'severity': 'Moderate',
        'confidence': 89.1,
        'description': 'Bacterial spot is a bacterial disease causing brown water-soaked lesions on pepper leaves and fruit.',
        'causes': 'Caused by Xanthomonas campestris pv. vesicatoria bacteria, spread by rain and overhead irrigation.',
        'symptoms': 'Small brown lesions with yellow halos on leaves, fruit develops brown raised pustules, premature defoliation.',
        'treatment': 'Apply copper bactericides at first sign of disease. Remove affected leaves and fruit. Improve air circulation.',
        'prevention': 'Avoid overhead irrigation. Use disease-resistant varieties. Practice crop rotation for 2-3 years.',
        'timeline': '2-3 weeks with bactericide treatment',
        'impact': 'Moderate to high fruit loss; significant cosmetic damage reduces marketability'
    },
    'Pepper,_bell___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 94.3,
        'description': 'This bell pepper leaf is completely healthy with excellent coloration and structure.',
        'causes': 'Proper greenhouse/field management and favorable conditions maintain this perfect state.',
        'symptoms': 'Vibrant green color, proper leaf morphology, no spots or lesions, strong integrity.',
        'treatment': 'No treatment needed. Continue with current care protocol.',
        'prevention': 'Maintain regular watering, fertilization, and disease monitoring schedule.',
        'timeline': 'Ongoing healthy plant growth',
        'impact': 'Maximum yield and fruit quality expected'
    },
    'Potato___Early_blight': {
        'disease': 'Early Blight',
        'severity': 'High',
        'confidence': 92.4,
        'description': 'Early blight is a fungal disease causing concentric circular lesions on potato leaves and stems.',
        'causes': 'Caused by Alternaria solani fungus, favored by warm, humid conditions and leaf wetness.',
        'symptoms': 'Circular lesions with concentric rings on lower leaves, yellow halo around lesions, premature leaf death.',
        'treatment': 'Apply fungicide at first sign of disease. Remove lower leaves to reduce infection. Improve air circulation.',
        'prevention': 'Use resistant potato varieties. Practice crop rotation for 3+ years. Plow under crop residue.',
        'timeline': '2-3 weeks with fungicide application',
        'impact': 'Moderate yield loss if untreated; can reduce tuber production by 20-30%'
    },
    'Potato___Late_blight': {
        'disease': 'Late Blight',
        'severity': 'Critical',
        'confidence': 95.8,
        'description': 'Late blight is a devastating fungal disease that can destroy entire potato crops, including stored tubers.',
        'causes': 'Caused by Phytophthora infestans oomycete, spread by rain splash and high humidity conditions.',
        'symptoms': 'Water-soaked lesions on leaves with white mold on undersides, rapid leaf collapse, black tuber rot.',
        'treatment': 'Apply fungicide immediately at first sign. Destroy infected plants. Improve drainage and air flow.',
        'prevention': 'Use resistant varieties. Destroy cull piles and wild potatoes. Ensure proper seed certification.',
        'timeline': '1-2 weeks with intensive fungicide program',
        'impact': 'Complete crop failure possible; disease can cause tuber loss in storage'
    },
    'Potato___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 96.5,
        'description': 'This potato leaf displays perfect health with no disease or pest damage visible.',
        'causes': 'Excellent cultural practices and favorable weather conditions maintain this ideal state.',
        'symptoms': 'Natural green color, proper leaf form and size, no spots or lesions, strong structure.',
        'treatment': 'No treatment needed. Continue with standard potato management practices.',
        'prevention': 'Maintain regular monitoring, proper irrigation, and pest surveillance.',
        'timeline': 'Ongoing healthy crop production',
        'impact': 'Maximum tuber yield and quality expected'
    },
    'Raspberry___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 95.1,
        'description': 'This raspberry leaf is in excellent health with no signs of disease or pest infestation.',
        'causes': 'Optimal growing conditions, proper care practices, and good genetics maintain this perfect state.',
        'symptoms': 'Natural vibrant green color, proper leaf dimensions, no damage or discoloration, intact structure.',
        'treatment': 'No treatment required. Maintain routine raspberry patch care.',
        'prevention': 'Continue with regular watering, pruning, and disease monitoring practices.',
        'timeline': 'Ongoing healthy raspberry cultivation',
        'impact': 'Excellent berry production and quality expected'
    },
    'Soybean___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 96.8,
        'description': 'This soybean leaf shows no signs of disease, pest damage, or nutritional deficiency.',
        'causes': 'Excellent field management, proper nutrition, and favorable conditions support this healthy state.',
        'symptoms': 'Proper green coloration, normal leaf size and form, no lesions or spots, strong structural integrity.',
        'treatment': 'No treatment needed. Maintain current crop management practices.',
        'prevention': 'Continue with integrated pest management and regular field monitoring.',
        'timeline': 'Ongoing healthy soybean growth',
        'impact': 'Maximum seed yield potential expected'
    },
    'Squash___Powdery_mildew': {
        'disease': 'Powdery Mildew',
        'severity': 'Moderate',
        'confidence': 88.7,
        'description': 'Powdery mildew is a fungal disease creating white powder coating on squash leaves, reducing photosynthesis.',
        'causes': 'Caused by Erysiphe cichoracearum fungus, favored by warm days, cool nights, and crowded plants.',
        'symptoms': 'White powdery coating on both leaf surfaces, leaf curling and yellowing, eventual leaf death.',
        'treatment': 'Apply sulfur dust or fungicide sprays weekly. Remove heavily infected leaves. Improve air circulation.',
        'prevention': 'Maintain proper plant spacing. Avoid excessive nitrogen. Use resistant squash varieties.',
        'timeline': '1-2 weeks with regular fungicide application',
        'impact': 'Moderate fruit loss; affects fruit quality and ripening'
    },
    'Strawberry___Leaf_scorch': {
        'disease': 'Leaf Scorch',
        'severity': 'Moderate',
        'confidence': 87.2,
        'description': 'Leaf scorch is a fungal disease causing red-purple lesions that eventually turn brown on strawberry leaves.',
        'causes': 'Caused by Diplocarpon earlianum fungus, spread by rain splash and high humidity conditions.',
        'symptoms': 'Small red-purple spots on leaves that enlarge to brown lesions with purple margins.',
        'treatment': 'Remove and destroy infected leaves. Apply fungicide sprays at first sign of disease.',
        'prevention': 'Use resistant strawberry varieties. Remove runners to improve air circulation. Practice crop rotation.',
        'timeline': '2-3 weeks with fungicide treatment',
        'impact': 'Moderate fruit loss; affects plant vigor and winter survival'
    },
    'Strawberry___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 94.9,
        'description': 'This strawberry leaf exhibits perfect health with no visible disease or pest damage.',
        'causes': 'Proper strawberry patch management and favorable conditions maintain this excellent state.',
        'symptoms': 'Natural green color, proper leaf morphology, no lesions or spots, strong structure.',
        'treatment': 'No treatment needed. Continue with routine strawberry bed maintenance.',
        'prevention': 'Maintain regular watering, weeding, and disease monitoring schedule.',
        'timeline': 'Ongoing healthy strawberry cultivation',
        'impact': 'Excellent berry quality and productivity expected'
    },
    'Tomato___Bacterial_spot': {
        'disease': 'Bacterial Spot',
        'severity': 'High',
        'confidence': 90.6,
        'description': 'Bacterial spot is a bacterial disease causing small dark lesions on tomato leaves and fruit.',
        'causes': 'Caused by Xanthomonas species bacteria, spread by rain splash, insects, and contaminated tools.',
        'symptoms': 'Small dark water-soaked lesions on leaves with yellow halos, fruit develops raised brown pustules.',
        'treatment': 'Apply copper bactericides at first sign. Remove infected leaves and fruit. Avoid overhead irrigation.',
        'prevention': 'Use disease-resistant tomato varieties. Practice 3-year crop rotation. Disinfect stakes and tools.',
        'timeline': '2-3 weeks with bactericide treatment',
        'impact': 'Moderate to high fruit loss; significant marketability reduction'
    },
    'Tomato___Early_blight': {
        'disease': 'Early Blight',
        'severity': 'High',
        'confidence': 91.3,
        'description': 'Early blight is a fungal disease causing concentric circular lesions on tomato leaves and stems.',
        'causes': 'Caused by Alternaria solani fungus, spread by soil splash and high humidity conditions.',
        'symptoms': 'Concentric ring patterns on leaves starting on lower foliage, yellow halo around lesions, premature defoliation.',
        'treatment': 'Remove lower leaves and infected fruit. Apply fungicide regularly. Improve air circulation.',
        'prevention': 'Use resistant varieties. Mulch to prevent soil splash. Practice 3-year crop rotation.',
        'timeline': '2-3 weeks with fungicide program',
        'impact': 'Moderate fruit loss; severe defoliation can stunt plant growth'
    },
    'Tomato___Late_blight': {
        'disease': 'Late Blight',
        'severity': 'Critical',
        'confidence': 93.7,
        'description': 'Late blight is a devastating fungal disease that rapidly destroys tomato foliage and fruit.',
        'causes': 'Caused by Phytophthora infestans oomycete, spread by rain and high humidity in cool conditions.',
        'symptoms': 'Water-soaked lesions on leaves with white mold on undersides, rapid collapse of foliage, fruit rot.',
        'treatment': 'Apply fungicide immediately at first sign. Remove infected plant material. Improve air circulation.',
        'prevention': 'Use resistant varieties. Avoid overhead watering. Remove infected volunteers and wild potatoes.',
        'timeline': '1-2 weeks with intensive fungicide application',
        'impact': 'Severe fruit loss; can cause complete crop failure'
    },
    'Tomato___Leaf_Mold': {
        'disease': 'Leaf Mold',
        'severity': 'Moderate',
        'confidence': 86.8,
        'description': 'Leaf mold is a fungal disease causing yellow spots on upper tomato leaves with olive-green mold below.',
        'causes': 'Caused by Cladosporium fulvum fungus, favored by high humidity and poor air circulation.',
        'symptoms': 'Yellow blotches on upper leaf surface, olive-green mold on undersides, severe defoliation if untreated.',
        'treatment': 'Apply fungicide at first sign. Prune lower leaves. Improve greenhouse ventilation and reduce humidity.',
        'prevention': 'Use resistant varieties. Maintain proper spacing. Control humidity and ensure air circulation.',
        'timeline': '2-3 weeks with fungicide treatment',
        'impact': 'Moderate fruit loss; primarily affects plant vigor and fruit production'
    },
    'Tomato___Septoria_leaf_spot': {
        'disease': 'Septoria Leaf Spot',
        'severity': 'Moderate',
        'confidence': 88.1,
        'description': 'Septoria leaf spot is a fungal disease causing small circular lesions with dark borders on tomato leaves.',
        'causes': 'Caused by Septoria lycopersici fungus, spread by rain splash and overhead irrigation.',
        'symptoms': 'Small circular lesions with gray centers and dark borders, black pycnidia in lesion centers.',
        'treatment': 'Remove infected leaves and lower foliage. Apply fungicide regularly. Avoid overhead watering.',
        'prevention': 'Use resistant varieties. Practice crop rotation for 3+ years. Mulch to prevent soil splash.',
        'timeline': '2-3 weeks with fungicide program',
        'impact': 'Moderate fruit loss; severe defoliation affects fruit ripening and sugar content'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'disease': 'Two-Spotted Spider Mites',
        'severity': 'High',
        'confidence': 89.5,
        'description': 'Spider mites are tiny arthropods that feed on tomato leaf cells, causing stippling and webbing.',
        'causes': 'Caused by Tetranychus urticae mites, favor warm, dry conditions and can reproduce rapidly.',
        'symptoms': 'Fine yellow stippling on leaves, fine webbing on leaf undersides, severe bronzing, premature leaf drop.',
        'treatment': 'Apply miticide sprays. Increase humidity through misting. Introduce predatory mites for biological control.',
        'prevention': 'Maintain adequate humidity. Avoid excessive nitrogen fertilization. Regular leaf spraying with water.',
        'timeline': '1-2 weeks with miticide treatment',
        'impact': 'Moderate to high damage if untreated; affects photosynthesis and fruit development'
    },
    'Tomato___Target_Spot': {
        'disease': 'Target Spot',
        'severity': 'Moderate',
        'confidence': 87.4,
        'description': 'Target spot is a fungal disease causing circular lesions with concentric rings resembling a target.',
        'causes': 'Caused by Corynespora cassiicola fungus, spread by rain splash in warm, humid conditions.',
        'symptoms': 'Circular lesions with concentric dark rings on leaves and fruit, yellow halo surrounding lesions.',
        'treatment': 'Apply fungicide at first sign of disease. Remove infected leaves. Improve air circulation.',
        'prevention': 'Use resistant varieties. Avoid overhead irrigation. Maintain proper plant spacing.',
        'timeline': '2-3 weeks with fungicide application',
        'impact': 'Moderate fruit loss; affects fruit marketability'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'disease': 'Tomato Yellow Leaf Curl Virus',
        'severity': 'Critical',
        'confidence': 92.1,
        'description': 'TYLCV is a viral disease transmitted by whiteflies, causing severe yellowing and curling of tomato leaves.',
        'causes': 'Caused by Tomato yellow leaf curl virus transmitted by Bemisia tabaci whiteflies.',
        'symptoms': 'Yellowing and curling of young leaves, stunted plant growth, flower and fruit drop.',
        'treatment': 'No cure for infected plants. Control whitefly populations with insecticides. Remove infected plants.',
        'prevention': 'Use resistant varieties. Control whitefly populations with insecticides. Use reflective mulches.',
        'timeline': 'No cure; plants remain infected',
        'impact': 'Severe crop loss; infected plants become unproductive'
    },
    'Tomato___Tomato_mosaic_virus': {
        'disease': 'Tomato Mosaic Virus',
        'severity': 'High',
        'confidence': 90.9,
        'description': 'Tomato mosaic virus causes mottling and severe leaf distortion on tomato plants.',
        'causes': 'Caused by Tomato mosaic virus spread by contact, contaminated tools, and hands.',
        'symptoms': 'Mottling and mosaic patterns on leaves, leaf curling and distortion, stunted plant growth.',
        'treatment': 'No cure; remove infected plants immediately. Disinfect tools with bleach solution (1:9 ratio).',
        'prevention': 'Use resistant varieties. Practice good sanitation. Disinfect tools regularly. Don\'t smoke near plants.',
        'timeline': 'No cure; plants remain infected',
        'impact': 'High crop loss; severe stunting and reduced productivity'
    },
    'Tomato___healthy': {
        'disease': 'Healthy',
        'severity': 'None',
        'confidence': 97.3,
        'description': 'This tomato leaf shows perfect health with no disease or pest damage visible.',
        'causes': 'Excellent growing conditions, proper care, and regular monitoring maintain this ideal state.',
        'symptoms': 'Natural vibrant green color, proper leaf morphology, no spots or lesions, strong structural integrity.',
        'treatment': 'No treatment needed. Continue with routine tomato care practices.',
        'prevention': 'Maintain regular monitoring, proper watering, and disease surveillance schedule.',
        'timeline': 'Ongoing healthy tomato production',
        'impact': 'Maximum fruit yield and quality expected'
    }
}

# Health status categories
SEVERITY_LEVELS = {
    'None': '#2E7D32',          # Green - Healthy
    'Low': '#4CAF50',           # Light green
    'Moderate': '#FF9800',      # Orange
    'High': '#FFC107',          # Amber
    'Critical': '#D32F2F'       # Red
}

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Leaf Disease Detection System API",
        "version": "1.0.0",
        "status": "Running"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Leaf Disease Detection API",
        "version": "1.0.0"
    }

# Get all available classes
@app.get("/api/classes")
async def get_classes():
    return {
        "total_classes": len(CLASS_LABELS),
        "classes": CLASS_LABELS
    }

# Predict disease from image
@app.post("/api/predict")
async def predict_disease(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Load image
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image = image.resize((256, 256))

        # Convert to array
        img_array = np.array(image)

        # Same preprocessing used during training
        img_array = preprocess_input(img_array)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # Prediction
        predictions = model.predict(img_array, verbose=0)

        predicted_class_id = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0]) * 100)

        predicted_class_name = CLASS_LABELS[int(predicted_class_id)]

        # Top 3 predictions (helps debugging)
        top3_indices = np.argsort(predictions[0])[-3:][::-1]

        top3_predictions = [
            {
                "class": CLASS_LABELS[int(idx)],
                "confidence": round(float(predictions[0][idx] * 100), 2)
            }
            for idx in top3_indices
        ]

        suggestion_data = DISEASE_SUGGESTIONS.get(
            predicted_class_name,
            DISEASE_SUGGESTIONS["Tomato___healthy"]
        )

        return {
            "success": True,
            "predicted_class_id": int(predicted_class_id),
            "predicted_class": predicted_class_name,
            "confidence": round(confidence, 2),
            "top3_predictions": top3_predictions,

            "disease": suggestion_data["disease"],
            "severity": suggestion_data["severity"],
            "severity_color": SEVERITY_LEVELS.get(
                suggestion_data["severity"],
                "#2E7D32"
            ),
            "description": suggestion_data["description"],
            "causes": suggestion_data["causes"],
            "symptoms": suggestion_data["symptoms"],
            "treatment": suggestion_data["treatment"],
            "prevention": suggestion_data["prevention"],
            "timeline": suggestion_data["timeline"],
            "impact": suggestion_data["impact"]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
@app.get("/api/suggestions/{disease_name}")
async def get_suggestions(disease_name: str):
    suggestion = DISEASE_SUGGESTIONS.get(disease_name)
    if suggestion:
        return {
            "success": True,
            "disease_name": disease_name,
            "data": suggestion
        }
    else:
        return {
            "success": False,
            "error": "Disease not found",
            "message": f"No suggestions found for {disease_name}"
        }

# Get all suggestions
@app.get("/api/all-suggestions")
async def get_all_suggestions():
    return {
        "total_suggestions": len(DISEASE_SUGGESTIONS),
        "suggestions": DISEASE_SUGGESTIONS
    }

# About endpoint
@app.get("/api/about")
async def about():
    return {
        "name": "Leaf Disease Detection System",
        "version": "1.0.0",
        "description": "AI-powered system for detecting plant diseases from leaf images",
        "technologies": ["FastAPI", "TensorFlow", "Keras", "React", "Python"],
        "supported_classes": 38,
        "author": "Agriculture AI Team"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
