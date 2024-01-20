# 173. 1. Introduction

## Introduction
- **Purpose**: AWS offers a range of pre-trained AI services for integrating natural language and visual understanding into applications.
- **Complexity**: Processing natural language and visual data is complex, requiring advanced AI solutions.

## AWS AI Services Overview

### Amazon Transcribe
- **Function**: Converts speech to text.
- **Application**: Essential for making audio data searchable and analyzable.

### Amazon Translate
- **Function**: Translates text between languages.
- **Uses**: Useful for understanding foreign language comments and localizing products.

### Amazon Comprehend
- **Capabilities**:
  - Sentiment analysis.
  - Custom text classification.
  - Document grouping by topics.
  - Extracting medical information.
- **Purpose**: Analyzes text to discern intent and context.

### Amazon Polly
- **Description**: Text-to-speech service.

### Amazon Lex
- **Function**: Powers conversational interfaces like chatbots.
- **Interaction**: Allows both voice and text-based communication.
- **Background**: Underlies Amazon's Alexa consumer products.

### Amazon Rekognition
- **Function**: Analyzes image and video content.
- **Features**: Identifies objects, people, facial expressions, and inappropriate content; tracks people across frames.

### Amazon Textract
- **Function**: Extracts text and data from documents.
- **Compatibility**: Works with scanned images, PDFs, and more.

### Amazon DeepLens
- **Description**: A deep learning-enabled video camera for developers.
- **Purpose**: A tool for building and testing vision-enabled applications.

## Conclusion
- AWS AI services provide tools for building sophisticated applications capable of understanding and interacting through voice, text, images, and videos.
- These pre-trained services simplify the integration of complex AI capabilities into various applications.

# 174. 2.1 Amazon Transcribe and Lab

## Introduction to Amazon Transcribe
- **Purpose**: Converts recorded speech into text.
- **Importance**: Makes audio data searchable and analyzable for various applications.

## Use Cases for Amazon Transcribe
- Transcribing customer service calls.
- Generating closed captions and subtitles for videos.
- Enabling text search on audio/video archives.
- Analyzing text for intent and meaning in conversations.
- Converting audio and video content to local languages.

## Lab Overview: Transcribing an Audio File
- **Sample Audio File**: "XGBoost Audio Sample.wav" provided in the course.
- **Objective**: Use Transcribe to convert the audio content to text and compare with actual text.

### Steps to Transcribe Audio
1. **Login to AWS Management Console**: Access the Transcribe service.
2. **Real-Time Transcription Option**: Allows for instant transcription via computer mic.
3. **Batch Transcription**: Utilizes stored media in S3 for transcription.
4. **Upload Audio to S3**: Store the sample audio file in an S3 bucket (e.g., `chandra-ml-sagemaker`).
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

# 175. 2.2 Amazon Transcribe and Lab

## Overview
- **Objective**: Enhance Amazon Transcribe's accuracy by using custom vocabulary.
- **Context**: Addressing missed words and phrases in the transcription process.

## Custom Vocabulary Options
1. **Vocabulary List**: Text file with words for Transcribe to detect.
   - **Formatting**:
     - Hyphens for phrases (e.g., "Los-Angeles").
     - Dots for acronyms (e.g., "F.B.I.").
   - **Example**: Adding "X.G.-Boost" for "XGBoost".

2. **Vocabulary Table**: Provides additional pronunciation and display information.
   - **Columns**:
     - Phrase: Word/phrase to recognize.
     - IPA: International Phonetic Alphabet notation.
     - Sounds Like: Breakdown of word pronunciation.
     - Display As: Desired output format.
   - **Usage**: Specify either IPA or Sounds Like, not both.

## Creating and Using Custom Vocabulary
1. **Upload Vocabulary Files to S3**: Place `VocabularyList.txt` and `VocabularyTable.txt` in an S3 bucket.
2. **Create Custom Vocabulary in Transcribe Console**:
   - Name the vocabulary (e.g., "xgboost-list", "xgboost-table").
   - Select the corresponding file from S3.
3. **Transcription Job with Custom Vocabulary**:
   - Create a copy of the original transcription job.
   - Select the newly created custom vocabulary.
   - Analyze the improved output.

## Results and Observations
- **With Vocabulary List**: Improved detection of phrases like "XGBoost" and "tree-based".
- **With Vocabulary Table**: Better output format, correct spellings (e.g., "XGBoost").
- **Limitations**: May require further refinement to understand specific accents or pronunciations.

## Conclusion
- Custom vocabulary significantly improves Transcribe's performance for domain-specific words and abbreviations.
- Essential for applications requiring high transcription accuracy.
- Human supervision recommended for critical content to ensure quality.

# 176. 3. Amazon Translate

## Introduction to Amazon Translate
- **Purpose**: Translates text between languages.
- **Applications**: Understanding foreign language reviews/comments, product/service localization.
- **Features**: Neural network-based, context-aware translation for accuracy and fluency.
- **Modes**: Supports real-time and batch translation.

## Amazon Translate Lab Overview
- **Goal**: Explore the capabilities of Amazon Translate in different scenarios.
- **Access**: Through AWS management console.

### Real-Time Translation
- **Process**: Input source text and select target language for translation.
- **Auto-Detect**: Feature to automatically identify the source language.

### Lab Experiment
1. **Simple Test**: Translate "Hello World" to Hindi and Spanish.
2. **Quality Verification**: Use Google Translate to cross-check translations.
3. **Complex Example**: Translate XGBoost text to Hindi and Spanish, verify with Google Translate.

### Observations
- **Accuracy**: High-quality translations with preserved meaning.
- **Recovery of Original Text**: Successful retrieval of the original text using Google Translate.
- **Impact of Input Quality**: The quality of input text (from transcription) can affect translation accuracy.

### Testing with Poor Transcription
- **Experiment**: Translate text with errors (from default transcribe settings) and reverse-translate.
- **Result**: Poor input leads to inaccurate translations, highlighting the need for quality input.

## Conclusion
- Amazon Translate offers precise and fluent translations, effective for a variety of use cases.
- Verification with an external service like Google Translate confirms the accuracy.
- Input quality is crucial; poor transcription can lead to compounded errors in translation.
- Human supervision recommended for ensuring high-quality translations.

## Recommendations
- Experiment with Amazon Translate for various language translation needs.
- Use the course forum for feedback and sharing experiences with the service.

# 178. 4.1 Amazon Comprehend

## Introduction to Amazon Comprehend
- **Purpose**: Analyzes text data to extract insights.
- **Capabilities**: Sentiment analysis, custom classification, medical information recognition, syntax analysis.

## Amazon Comprehend Capabilities Overview
- **Entity Recognition**: Identifies entities like organizations, cities, dates, and provides confidence scores.
- **Key Phrase Detection**: Extracts important phrases or topics from text.
- **Language Detection**: Automatically identifies the language of the text.
- **Sentiment Analysis**: Determines the overall sentiment (positive, negative, neutral, mixed).
- **Syntax Analysis**: Breaks down text into parts of speech.

## Hands-on Lab with Comprehend
1. **Accessing Comprehend**: Navigate to the Comprehend service in AWS Management Console.
2. **Real-Time Analysis**: Use the console for immediate text analysis.
3. **Sample Text Analysis**:
   - Example Text: Analysis of XGBoost and Kaggle-related text.
   - Detected Entities: Categorizes "XGBoost" as an organization with varying confidence scores.
   - Sentiment: Neutral with slight positive bias.

### Sentiment Analysis Examples
- **Sample 1**: "The movie is surprising with plenty of unsettling plot twists."
  - Comprehend Result: Positive sentiment.
- **Sample 2**: "I love my mobile but would not recommend it to any of my colleagues."
  - Comprehend Result: Mixed sentiment.
- **Sample 3**: "Pastel colored 1980s day cruisers from Florida are ugly."
  - Comprehend Result: Negative sentiment.

### Medical Text Analysis
- **Utility**: Extracts meaningful information from unstructured health records.
- **Example**: Analysis of a simple medical text.
- **Results**: Categorization into diagnosis, medicine, dosage, frequency, etc.
- **Note**: Possible permission errors, retry or contact AWS support if persistent.

## Summary
- Amazon Comprehend provides robust text analysis capabilities, offering insights into sentiment, syntax, and key phrases.
- Effective for both general and medical text analysis.
- Custom classification capabilities to be explored in the next lecture.

# 179. Pricing Comprehend

## Overview of Custom Model Costs
- **Non-Free Tier**: Training custom models with Amazon Comprehend incurs charges.
- **Charge Estimate for Labs**: Approximately USD 2-3 for upcoming lab exercises.
- **Maintenance Charge**: USD 0.50 per month for each trained model.

## Detailed Pricing Structure
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

## Key Takeaways
- Utilizing Amazon Comprehend's custom model features will incur costs outside the AWS free-tier.
- Users should be aware of both the training costs and ongoing model management fees.
- Pricing details are available on the [Amazon Comprehend Pricing Page](https://aws.amazon.com/comprehend/pricing/).

## Considerations for Users
- Plan and budget for the training and management of custom models in Amazon Comprehend.
- Ensure endpoints are deleted when not in use to avoid unnecessary charges.

# 180. 4.2 Amazon Comprehend

## Objective
- Create a classifier to identify tweets requiring follow-up using Amazon Comprehend.

## Use Cases for Classifier
- Moderating comments and reviews.
- Categorizing documents into user-defined categories.

## Lab Overview: Twitter Classification Dataset
- **Dataset**: AWS-provided data with regular tweets and those needing follow-up.
- **Location**: AWS S3 bucket `social-media` folder.
- **Task**: Classify tweets needing follow-up (labeled as '1') from normal tweets (labeled as '0').

## Data Preparation Steps
1. **Access AWS Management Console**: Start a SageMaker notebook instance.
2. **Update IAM Role Permissions**: Attach `AmazonS3ReadOnlyAccess` policy for S3 access.
3. **Download Dataset**: Retrieve dataset from the specified S3 bucket.
4. **Dataset Examination**: Analyze the dataset comprising 10,000 tweets with 45 columns.
   - **Key Columns**: 'text' (tweet content) and 'training label' (follow-up required or not).

## Examples from Dataset
- **Positive Tweets**: Indicate a need for follow-up, including complaints and feature requests.
- **Negative Tweets**: Normal tweets without follow-up requirements.
- **Labeling Quality**: Some misclassifications observed.

## Test Data Reservation
- **Splitting Data**: Reserve 10% for testing (1,000 tweets), use 90% (9,000 tweets) for training/validation.
- **Comprehend's Internal Use**: 80% of provided data for training, 20% for validation.

## File Format for Comprehend
- **CSV Format**: Label in the first column, followed by the tweet text.
- **No Header**: Ensure no headers are included in the file.
- **File Creation**: Two versions of the test file - with and without labels.

## S3 Bucket Preparation
- **Specify Bucket**: Upload training and test files to a user-defined S3 bucket.

## Conclusion
- The lab sets the stage for training a model in Amazon Comprehend with a focus on data preparation.
- The next lecture will cover the actual model training process using the prepared data.

# 181. 4.3 Amazon Comprehend training

## Building a Custom Classifier
- **Objective**: Classify Twitter tweets requiring follow-up using Amazon Comprehend.
- **Data**: AWS-provided Twitter dataset with regular and follow-up tweets.

## Steps to Build the Classifier
1. **Access Comprehend Management Console**: Ensure the same AWS region as the S3 bucket.
2. **Custom Classifier Creation**: 
   - Name: `Twitter follow up`.
   - Language: English.
   - Training Data: CSV file from S3 containing tweets and labels.

3. **Role Permission**: Create an IAM role for Comprehend to access S3 files.

## Model Training and Metrics
- **Training**: Comprehend uses 8,100 documents for training and 900 for validation.
- **Metrics**:
  - Precision: 0.86
  - Recall: 0.81
  - F1 Score: 0.83

## Batch Prediction
1. **Analysis Job Setup**: 
   - Name: `Twitter test`.
   - Analysis Type: Custom Classification.
   - Classifier: `Twitter follow up`.
   - Test Data: Specified from S3.
2. **Output Review**: Analyze predictions stored in S3.

## Prediction Analysis
- **Confusion Matrix Evaluation**: 
  - True Positives: 93
  - False Positives: 24
  - True Negatives: 827
  - False Negatives: 56
- **Performance**: Missed 38% of positive tweets, 3% false alarms.

## Finding Optimal Cutoff Based on Business Costs
- **Cost Assumptions**:
  - Following up a tweet: $10.
  - Missed opportunity (False Negative): $30.
- **Optimal Cutoff Analysis**: The lowest cost at a cutoff of 0.21.
- **Improved Performance**: Increased detection of positive tweets to 77% (up from 62%).

## Conclusion
- **Comprehend for Text Classification**: Effective tool with minimal setup effort.
- **Cutoff Optimization**: Business-cost based approach enhances classifier effectiveness.
- **Lab Outcome**: Demonstrated the creation, training, and optimization of a custom text classifier.

# 182. 5. Amazon Polly

## Introduction to Amazon Polly
- **Purpose**: Converts text into lifelike speech.
- **Applications**: Building speech-enabled products and applications.
- **Capabilities**:
  - Real-time and batch audio stream generation.
  - Variety of voices and languages.
  - Customizable speech synthesis using SSML (Speech Synthesis Markup Language).

## Hands-On Lab with Amazon Polly
1. **Accessing Polly**: Navigate to Polly in the AWS Management Console.
2. **Text Input**: Use a standard example text from previous lectures.
3. **Voice Selection**: Experiment with different voices and accents.
4. **Engine Types**:
   - Standard: Basic text-to-speech conversion.
   - Neural: Enhanced quality for more lifelike speech.

### Audio Generation and Comparison
- **Joanna (US English)**: Compare standard and neural engine outputs.
- **Regional Voices**: Listen to audio generated with different regional accents.
- **Language Translation**: Translate text with Amazon Translate and synthesize in the translated language.
- **Spanish Example**: Demonstrate speech generation for a Spanish translation.

### Observations
- **Quality**: Neural engine provides a more natural and fluid speech compared to the standard engine.
- **Regional Variations**: Distinct differences in accents and pronunciation styles.
- **Translation and Speech Synthesis**: Effective for localization of content.

### Customization and Quality Improvement
- **SSML Markup**: Customize aspects like speaking style, pronunciation, and speed.
- **Quality Enhancement**: Necessary to refine speech for a more natural flow.

## Conclusion
- Amazon Polly offers a quick and versatile solution for text-to-speech needs.
- While the service provides a range of voices and customization options, quality refinement is essential for optimal results.

## Recommendations
- Experiment with Polly and Translate for product localization and other speech-enabled applications.
- Share feedback and experiences with the service for further exploration.

# 183. 6. Amazon Lex

## Introduction to Amazon Lex
- **Purpose**: Build conversational interfaces using voice and text.
- **Integration**: Combines speech recognition, natural language processing, and business logic.
- **Usage**: Powers Amazon Alexa and other consumer products.

## Key Features of Lex
- **Speech Recognition**: Converts speech to text.
- **Natural Language Processing (NLP)**: Understands user intent.
- **Lambda Integration**: Triggers relevant business logic.
- **Communication**: Responds with voice or text.

## Understanding Lex with Hotel Booking Example
1. **Utterance**: User message expressing interest in booking.
2. **Intent**: Lex invokes an intent (e.g., book a hotel).
3. **Slots**: Collects additional information (e.g., city, dates).
4. **Fulfillment**: Completes the booking with all required data.

## Hands-On Lab with Amazon Lex
1. **Access Lex Console**: Navigate to Lex in AWS Management Console.
2. **Create a Bot**: Example bot for booking trips.
3. **Utterances and Intents**:
   - Car Booking: Recognizes specific phrases for booking cars.
   - Hotel Booking: Recognizes phrases for booking hotels.
4. **Data Collection**: Defines slots for required information (city, dates, car type, etc.).
5. **DataType Specification**: Sets data types for each slot (e.g., city, date).
6. **Confirmation Prompt**: User can confirm or cancel the booking.
7. **Lambda Integration**: Optional for business logic execution.

### Testing the Bot
- **Text Interaction**: Enter phrases like "car rental" to initiate booking.
- **Voice Interaction**: Speak to the bot using a computer mic.
- **Slot Filling**: Lex automatically converts natural language inputs to slot values.
- **Fulfillment Response**: Notifies when the request is ready for fulfillment.

## Conclusion
- Amazon Lex offers a powerful framework for creating voice and text-based conversational applications.
- It simplifies integration of speech recognition, NLP, and response generation.

# 184. 7. Amazon Rekognition

## Introduction to Amazon Rekognition
- **Purpose**: Analyzes images and videos to identify objects, scenes, activities, and more.
- **Applications**: Object detection, facial recognition, content moderation, celebrity identification, text extraction.

## Hands-On Lab with Rekognition
- **Access Rekognition**: Navigate to the Rekognition service in AWS Management Console.
- **Object and Scene Detection**: Analyze images to identify objects and describe scenes.

### Image Analysis Examples
1. **Automobiles and Sports**: Detected various vehicles, person, skateboard, and associated the scene with sports.
2. **City Skyline**: Identified urban environment, city, highrise.
3. **Warplanes and Bombers**: Recognized aircraft, misinterpreted as warplanes.
4. **Cat**: Precisely identified breed as Abyssinian cat.

### Image Moderation
- **Safe Image**: No moderation labels detected.
- **Flagged Image**: Identified as suggestive due to swimwear.

### Facial Analysis
- Identifies attributes like gender, age range, and expression for each person in a photo.
- **Provided Examples**: Analyzes individual attributes in group pictures.

### Celebrity Recognition
- **Accuracy**: Quick and accurate identification of celebrities.
- **Personal Test**: Attempted to identify the user's photo (not recognized as a celebrity).

### Face Comparison
- Compares faces for similarity in different images.
- **Results**: Varied similarity scores, including a high similarity with the user's brother.

### Text Detection in Images
- Extracts text from images, identifying phrases, fonts, and license plates.

## Video Analysis
- **Usage**: Analyze a video from social media.
- **Process**: Video uploaded and analyzed by Rekognition.
- **Results**: Detected people, objects, activities; unexpectedly flagged as containing violence.

## Conclusion
- Amazon Rekognition demonstrates powerful capabilities in image and video analysis.
- Applications range from object recognition to facial analysis and content moderation.
- Caution: AI conclusions can be unexpected, stressing the need for human supervision.

## Recommendations
- Experiment with Rekognition for diverse image and video analysis needs.
- Always incorporate human oversight in AI-driven applications, especially for sensitive content.

# 185. 8. Amazon Textract & Summary

## Introduction to Amazon Textract
- **Purpose**: Extract text, forms, and data from scanned documents.
- **Use Cases**:
  - Enable keyword search in scanned documents.
  - Detect personally identifiable information (PII) for compliance and security.

## Hands-On Example with Textract
1. **Access Textract**: Navigate to Textract in the AWS Management Console.
2. **Analyzing a Document**:
   - Sample Form: Extracts raw text, entry fields, and table data.
   - Process: Upload document for analysis by Textract.

### Document Analysis Examples
1. **AWS Machine Learning Specialty Exam Guide (PDF)**:
   - Content: Sections, tables, and varied text.
   - Textract Analysis: Run Textract on the PDF document.
   - Outcome: Partially successful extraction of text and tables.

### Results and Downloads
- **Raw Text**: Downloadable as a text file containing the content of the PDF.
- **Table Data**: Extracted and available in CSV format.
- **Potential Applications**: Feeding data into Elasticsearch or other search tools for document searchability.

## Conclusion
- Amazon Textract offers a straightforward solution for extracting information from various document formats.
- While the extraction process is not flawless, it provides a quick method to digitize and utilize document content.
- The cloud has made these specialized services accessible and easy to integrate into applications.

## Recommendations
- Explore Textract for document processing and data extraction in your projects.
- Consider integrating Textract with search and analysis tools for enhanced document management.
