# Artificial Intelligence (AI) Services

## Introduction (Lesson 173)

| Service | Description |
| ------- | ----------- |
| Transcribe | Converts speech to text. |
| Translate | Translates text between languages. |
| Comprehend | Analyzes text to discern intent and context. |
| .          | Sentiment analysis, Custom text classification, Document grouping by topics, Extracting medical information. |
| Polly | Text-to-speech service. |
| Lex | Powers conversational interfaces like chatbots. |
| .   | Allows both voice and text-based communication. |
| .   | Underlies Amazon's Alexa consumer products. |
| Rekognition | Analyzes image and video content. |
| .           | Identifies objects, people, facial expressions, and inappropriate content; tracks people across frames. |
| Textract | Extracts text and data from documents. |
| .       | Works with scanned images, PDFs, and more. |
| DeepLens | A deep learning-enabled video camera for developers. |
| .        | A tool for building and testing vision-enabled applications. |

## Amazon Transcribe (Lesson 174&175)

### Steps to Transcribe Audio
1. Login to AWS Management Console, look for Transcribe service.
2. **Real-Time Transcription Option**: Allows for instant transcription via computer mic.
3. **Transcription Jobs**: Allows batch transcription, utilizes stored media in S3 for transcription.
4. Upload the sample audio file in an S3 bucket.
5. **Create Transcription Job**: 
   - Name the job (e.g., "xgboost sample").
   - Input file location: S3 path of the audio file.
   - Format: WAV.
   - Output data: Amazon default.
6. **Review Transcribed Text**: Analyze the generated text, including confidence scores and timestamps.

### Initial Results
- **Transcription Quality**: The default transcription significantly altered the content's meaning.
- **Concerns**: Highlighted issues with accent interpretation by the service.
- **Request and Response Example**: Demonstrates application integration for transcription.

### Addressing missed words and phrases in the transcription process.

1. **Vocabulary List**: Text file with words for Transcribe to detect.
   - **Formatting**:
     - Hyphens for phrases (e.g., "Los-Angeles").
     - Dots for acronyms (e.g., "F.B.I.").
   - **Example**: Adding "X.G.-Boost" for "XGBoost".
2. **Upload Vocabulary Files to S3**: Place `VocabularyList.txt` in an S3 bucket.
3. **Create Custom Vocabulary in Transcribe Console**:
   - Name the vocabulary (e.g., "xgboost-list").
   - Select the corresponding file from S3.
4. **Transcription Job with Custom Vocabulary**:
   - Create a copy of the original transcription job.
   - Select the newly created custom vocabulary.
   - Analyze the improved output.
5. **Vocabulary Table**: Provides additional pronunciation and display information.
   - **Columns**:
     - Phrase: Word/phrase to recognize.
     - IPA: International Phonetic Alphabet notation.
     - Sounds Like: Breakdown of word pronunciation.
     - Display As: Desired output format.
   - **Usage**: Specify either IPA or Sounds Like, not both.

## Amazon Translate (Lesson 176)

- Supports real-time and batch translation.
- From AWS management console, navigate to Amazon Translate.
- **Real-Time Translation**:
  - **Process**: Input source text and select target language for translation.
  - **Auto-Detect**: Feature to automatically identify the source language.

## Amazon Comprehend

- Analyzes text data to extract insights.
- **Capabilities**: Sentiment analysis, custom classification, medical information recognition, syntax analysis.

### Lab-1 (Lesson 178)
1. **Accessing Comprehend**: Navigate to the Comprehend service in AWS Management Console.
2. **Real-Time Analysis**: Use the console for immediate text analysis.
3. **Sample Text Analysis**:
   - Example Text: Analysis of XGBoost and Kaggle-related text.
   - Detected Entities: Categorizes "XGBoost" as an organization with varying confidence scores.
   - Sentiment: Neutral with slight positive bias.

#### Amazon Comprehend Capabilities Overview
- **Entity Recognition**: Identifies entities like organizations, cities, dates, and provides confidence scores.
- **Key Phrase Detection**: Extracts important phrases or topics from text.
- **Language Detection**: Automatically identifies the language of the text.
- **Sentiment Analysis**: Determines the overall sentiment (positive, negative, neutral, mixed).
- **Syntax Analysis**: Breaks down text into parts of speech.

#### Medical Text Analysis
- **Utility**: Extracts meaningful information from unstructured health records.
- **Example**: Analysis of a simple medical text.
- **Results**: Categorization into diagnosis, medicine, dosage, frequency, etc.
- **Note**: Possible permission errors, retry or contact AWS support if persistent.

### Pricing Comprehend (Lesson 179)

- **Custom Comprehend APIs**: Used for training custom NLP models for text categorization and entity extraction.
- **Asynchronous Inference Requests**:
  - Charged per 100 characters.
  - Minimum charge: 3 units (300 characters) per request.
- **Model Training Charges**:
  - $3 per hour, billed by the second.
- **Model Management Fee**:
  - $0.50 per month per custom model.
- **Synchronous Inference Requests**:
  - Requires provisioning an endpoint with specified throughput.
  - Charges accrue from endpoint start time to deletion.
- Pricing details are available on the [Amazon Comprehend Pricing Page](https://aws.amazon.com/comprehend/pricing/).

### Lab-2 (Lesson 180&181)

- Create a classifier to identify tweets requiring follow-up using Amazon Comprehend.

#### Data Preparation Steps
1. Use SageMaker notebook instance.
2. Attach `AmazonS3ReadOnlyAccess` policy for S3 access.
3. Retrieve dataset from the specified S3 bucket.
4. Analyze the dataset comprising 10,000 tweets with 45 columns.
   - `text` (tweet content) and `training label` (follow-up required or not).

#### File Format for Comprehend
- **CSV Format**: Label in the first column, followed by the tweet text.
- **No Header**: Ensure no headers are included in the file.
- **File Creation**: Two versions of the test file - with and without labels.

#### Building a Custom Classifier
- **Objective**: Classify Twitter tweets requiring follow-up using Amazon Comprehend.
- **Data**: AWS-provided Twitter dataset with regular and follow-up tweets.

#### Steps to Build the Classifier
1. **Access Comprehend Management Console**: Ensure the same AWS region as the S3 bucket.
2. **Custom Classifier Creation**: 
   - Name: `Twitter follow up`.
   - Language: English.
   - Training Data: CSV file from S3 containing tweets and labels.
3. **Role Permission**: Create an IAM role for Comprehend to access S3 files.

#### Batch Prediction
- Name: `Twitter test`.
- Analysis Type: Custom Classification.
- Classifier: `Twitter follow up`.
- Test Data: Specified from S3.

## Amazon Polly (Lesson 182)

### Introduction to Amazon Polly
- **Purpose**: Converts text into lifelike speech.
- **Applications**: Building speech-enabled products and applications.
- **Capabilities**:
  - Real-time and batch audio stream generation.
  - Variety of voices and languages.
  - Customizable speech synthesis using SSML (Speech Synthesis Markup Language).

### Hands-On Lab with Amazon Polly
1. **Accessing Polly**: Navigate to Polly in the AWS Management Console.
2. **Text Input**: Use a standard example text from previous lectures.
3. **Voice Selection**: Experiment with different voices and accents.
4. **Engine Types**:
   - Standard: Basic text-to-speech conversion.
   - Neural: Enhanced quality for more lifelike speech.

### Customization and Quality Improvement
- **SSML Markup**: Customize aspects like speaking style, pronunciation, and speed.
- **Quality Enhancement**: Necessary to refine speech for a more natural flow.

## Amazon Lex (Lesson 183)

### Introduction to Amazon Lex
- **Purpose**: Build conversational interfaces using voice and text.
- **Integration**: Combines speech recognition, natural language processing, and business logic.
- **Usage**: Powers Amazon Alexa and other consumer products.

### Key Features of Lex
- **Speech Recognition**: Converts speech to text.
- **Natural Language Processing (NLP)**: Understands user intent.
- **Lambda Integration**: Triggers relevant business logic.
- **Communication**: Responds with voice or text.

### Understanding Lex with Hotel Booking Example
1. **Utterance**: User message expressing interest in booking.
2. **Intent**: Lex invokes an intent (e.g., book a hotel).
3. **Slots**: Collects additional information (e.g., city, dates).
4. **Fulfillment**: Completes the booking with all required data.

### Hands-On Lab with Amazon Lex
1. **Access Lex Console**: Navigate to Lex in AWS Management Console.
2. **Create a Bot**: Example bot for booking trips.
3. **Utterances and Intents**:
   - Car Booking: Recognizes specific phrases for booking cars.
   - Hotel Booking: Recognizes phrases for booking hotels.
4. **Data Collection**: Defines slots for required information (city, dates, car type, etc.).
5. **DataType Specification**: Sets data types for each slot (e.g., city, date).
6. **Confirmation Prompt**: User can confirm or cancel the booking.
7. **Lambda Integration**: Optional for business logic execution.

## Amazon Rekognition (Lesson 184)

### Introduction to Amazon Rekognition
- **Purpose**: Analyzes images and videos to identify objects, scenes, activities, and more.
- **Applications**: Object detection, facial recognition, content moderation, celebrity identification, text extraction.

### Hands-On Lab with Rekognition
- **Access Rekognition**: Navigate to the Rekognition service in AWS Management Console.
- **Object and Scene Detection**: Analyze images to identify objects and describe scenes.

### Image Analysis Examples
1. **Automobiles and Sports**: Detected various vehicles, person, skateboard, and associated the scene with sports.
2. **City Skyline**: Identified urban environment, city, highrise.
3. **Warplanes and Bombers**: Recognized aircraft, misinterpreted as warplanes.
4. **Cat**: Precisely identified breed as Abyssinian cat.

### Features
- **Image Moderation**: Safe Image. No moderation labels detected.
- **Facial Analysis**: Identifies attributes like gender, age range, and expression for each person in a photo.
- **Celebrity Recognition**: Quick and accurate identification of celebrities.
- **Face Comparison**: Compares faces for similarity in different images.
- **Text Detection in Images**: Extracts text from images, identifying phrases, fonts, and license plates.
- **Video Analysis**: Detects people, objects, activities

### Conclusion
- Caution: AI conclusions can be unexpected, stressing the need for human supervision.

## Amazon Textract (Lesson 185)

- Extract text, forms, and data from scanned documents.
- **Use Cases**:
  - Enable keyword search in scanned documents.
  - Detect personally identifiable information (PII) for compliance and security.

### Hands-On Example with Textract
1. **Access Textract**: Navigate to Textract in the AWS Management Console.
2. **Analyzing a Document**:
    - Sample Form: Extracts raw text, entry fields, and table data.
    - Process: Upload document for analysis by Textract.

### Document Analysis Examples
1. **AWS Machine Learning Specialty Exam Guide (PDF)**:
    - Content: Sections, tables, and varied text.
    - Textract Analysis: Run Textract on the PDF document.
    - Outcome: Partially successful extraction of text and tables.
2. Results and Downloads
    - **Raw Text**: Downloadable as a text file containing the content of the PDF.
    - **Table Data**: Extracted and available in CSV format.
    - **Potential Applications**: Feeding data into Elasticsearch or other search tools for document searchability.
