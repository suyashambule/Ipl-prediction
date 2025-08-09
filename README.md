# IPL Win Prediction System 🏏

A machine learning-powered application that predicts the probability of winning for teams during live IPL (Indian Premier League) cricket matches. This system analyzes current match conditions including score, target, overs, wickets, and team performance to provide real-time win probability predictions.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset Information](#dataset-information)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)

## 🎯 Project Overview

This IPL prediction system uses historical match data and machine learning algorithms to calculate the win probability for teams during the second innings of T20 cricket matches. The application takes into account various factors such as:

- Current score and target
- Overs completed and balls remaining
- Wickets fallen
- Team performance history
- Venue/city factors
- Current run rate vs required run rate

## ✨ Features

- **Real-time Predictions**: Get live win probability for both batting and bowling teams
- **Interactive Web Interface**: User-friendly Streamlit application
- **Comprehensive Team Data**: Supports all current IPL teams and venues
- **Historical Analysis**: Trained on extensive IPL match data from 2008 onwards
- **Multiple Factors**: Considers team strength, venue, match situation, and performance metrics
- **Instant Results**: Get probability percentages within seconds

## 📁 Project Structure

```
Ipl-prediction/
├── README.md                    # Project documentation
├── frontend.py                  # Streamlit web application
├── IPL prediction.ipynb         # Jupyter notebook for model development
├── matches.csv                  # Historical IPL match data
├── pipe.pkl                     # Trained machine learning pipeline
└── delivery.csv                 # Ball-by-ball delivery data (referenced in notebook)
```

## 🛠 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Ipl-prediction
```

### Step 2: Install Required Dependencies
```bash
pip install streamlit
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn
pip install pickle-mixin
```

### Alternative Installation (using requirements.txt)
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Web Application
1. Navigate to the project directory:
```bash
cd Ipl-prediction
```

2. Run the Streamlit application:
```bash
streamlit run frontend.py
```

3. Open your web browser and go to the provided local URL (usually `http://localhost:8501`)

4. Fill in the match details:
   - **Batting Team**: Select from dropdown of IPL teams
   - **Bowling Team**: Select the opposing team
   - **City**: Choose the match venue
   - **Target**: Enter the target score to chase
   - **Current Score**: Current runs scored by batting team
   - **Overs Completed**: Number of overs bowled
   - **Wickets Gone**: Number of wickets fallen

5. Click **"Predict Probability"** to get win percentages for both teams

### Using the Jupyter Notebook
1. Open the notebook:
```bash
jupyter notebook "IPL prediction.ipynb"
```

2. Run all cells to see:
   - Data exploration and analysis
   - Feature engineering process
   - Model training and evaluation
   - Performance metrics and visualizations

## 🤖 Model Details

### Features Used
The model considers the following key features:

- **batting_team**: The team currently batting
- **bowling_team**: The team currently bowling  
- **city**: Match venue location
- **runs_left**: Remaining runs needed to win
- **balls_left**: Remaining balls in the innings
- **wickets**: Wickets remaining for batting team
- **total_runs_x**: Target score
- **current_rate**: Current run rate (CRR)
- **required_rate**: Required run rate (RRR)

### Model Pipeline
The prediction pipeline includes:
1. **Data Preprocessing**: Cleaning and feature engineering
2. **Categorical Encoding**: Converting team names and cities to numerical format
3. **Feature Scaling**: Normalizing numerical features
4. **Machine Learning Model**: Trained classifier for probability prediction

### Calculations
- **Runs Left**: Target - Current Score
- **Balls Left**: 120 - (Overs × 6)
- **Wickets Remaining**: 10 - Wickets Gone
- **Current Run Rate**: Current Score ÷ Overs
- **Required Run Rate**: (Runs Left × 6) ÷ Balls Left

## 📊 Dataset Information

### Match Data (`matches.csv`)
- **Coverage**: IPL seasons from 2008 to present
- **Records**: 800+ matches
- **Features**: Match details, teams, venues, results, margins
- **Seasons**: Multiple IPL seasons including playoffs and finals

### Key Statistics
- **Teams Covered**: All 10 current IPL franchises
- **Venues**: 30+ cricket stadiums across India and international venues
- **Match Types**: League matches, playoffs, semifinals, finals
- **Historical Span**: 15+ years of IPL data

### Supported Teams
- Royal Challengers Bangalore
- Mumbai Indians  
- Kolkata Knight Riders
- Rajasthan Royals
- Chennai Super Kings
- Sunrisers Hyderabad
- Delhi Capitals
- Punjab Kings
- Lucknow Super Giants
- Gujarat Titans

### Supported Venues
Major cricket stadiums including:
- Bangalore, Delhi, Mumbai, Kolkata
- Chennai, Hyderabad, Jaipur, Pune
- International venues (UAE, South Africa)
- And 20+ other cricket venues

## 🛠 Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Pickle**: Model serialization
- **Jupyter**: Interactive development environment

## 📱 Screenshots

### Main Interface
The application provides an intuitive interface where users can:
- Select batting and bowling teams from dropdowns
- Choose the match venue
- Input current match statistics
- Get instant win probability predictions

### Prediction Output
Results are displayed as:
```
Batting Team - XX.XX%
Bowling Team - XX.XX%
```

## 📈 Model Performance

The model provides accurate probability predictions based on:
- Historical match outcomes under similar conditions
- Team performance statistics
- Venue-specific factors
- Match situation analysis

Detailed performance metrics and model evaluation can be found in the Jupyter notebook.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## 🔮 Future Enhancements

- [ ] **Player-specific Analysis**: Include individual player performance data
- [ ] **Weather Conditions**: Factor in weather and pitch conditions
- [ ] **Real-time Data Integration**: Connect to live match APIs
- [ ] **Advanced ML Models**: Implement deep learning models (LSTM, Neural Networks)
- [ ] **Mobile App**: Develop mobile application
- [ ] **Historical Comparison**: Compare with actual match outcomes
- [ ] **Team Form Analysis**: Include recent team performance trends
- [ ] **Toss Impact**: Factor in toss decision impact
- [ ] **Player Injuries**: Account for key player availability
- [ ] **Powerplay Analysis**: Separate predictions for different match phases

## 📊 How It Works

1. **Data Input**: User enters current match situation
2. **Feature Engineering**: System calculates derived metrics (run rates, pressure indicators)
3. **Model Prediction**: ML pipeline processes features and outputs probabilities
4. **Results Display**: Win percentages shown for both teams in real-time

## 🏆 Use Cases

- **Cricket Enthusiasts**: Get insights during live matches
- **Fantasy Cricket**: Make informed decisions for fantasy teams
- **Betting Analysis**: Understand match dynamics (for educational purposes)
- **Cricket Analytics**: Study team performance patterns
- **Sports Broadcasting**: Enhance commentary with data-driven insights

## ⚠️ Disclaimer

This application is for educational and entertainment purposes only. Cricket match outcomes depend on numerous unpredictable factors, and predictions should not be used for gambling or betting purposes. Past performance does not guarantee future results.

## 📞 Support

For questions, bug reports, or feature requests:
- Open an issue in the repository
- Contact the project maintainer
- Check the documentation in the Jupyter notebook

---

**Made with ❤️ for Cricket Analytics**

*Last Updated: 2024*
