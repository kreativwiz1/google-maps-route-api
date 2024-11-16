# Google Maps Route Estimation API 🗺️

A Flask-based REST API service that provides real-time route estimations using the Google Maps Directions API. Get detailed routing information between any two locations with support for various transportation modes.

## ✨ Features

- **Route Estimation**
  - Real-time calculations
  - Multiple transportation modes
    - 🚗 Driving
    - 🚶 Walking
    - 🚲 Cycling
    - 🚌 Transit
  - Detailed journey information
  - Alternative routes support

- **API Design**
  - RESTful architecture
  - JSON response format
  - Comprehensive error handling
  - Input validation

## 🛠️ Technical Stack

- Python 3.11
- Flask 3.0.0
- Gunicorn 21.2.0
- Requests 2.32.3

## 📋 Prerequisites

- Python 3.11+
- Poetry package manager
- Google Maps API key
- Basic REST API knowledge

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/google-maps-route-api.git
cd google-maps-route-api
```

2. Install dependencies:
```bash
poetry install
```

3. Configure Google Maps API key:
```bash
export GOOGLE_MAPS_API_KEY='your-api-key-here'
```

## 📡 API Reference

### Get Route Estimation

Retrieves detailed routing information between two locations.

#### Endpoint
```
POST /get-route-estimation
Content-Type: application/json
```

#### Request Body
```json
{
  "origin": "123 Main St, New York, NY",
  "destination": "456 Park Ave, New York, NY",
  "mode": "driving"
}
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| origin | string | Yes | Starting location |
| destination | string | Yes | Ending location |
| mode | string | No | Transportation mode (driving/walking/cycling/transit) |

#### Success Response
```json
{
  "routes": [{
    "legs": [{
      "distance": {
        "text": "1.2 km",
        "value": 1200
      },
      "duration": {
        "text": "5 mins",
        "value": 300
      },
      "steps": [
        {
          "distance": {"text": "0.2 km", "value": 200},
          "duration": {"text": "1 min", "value": 60},
          "html_instructions": "Head north on Main St",
          "travel_mode": "DRIVING"
        }
      ]
    }],
    "summary": "Main St and Park Ave"
  }],
  "status": "OK"
}
```

#### Error Response
```json
{
  "error": "Invalid request parameters",
  "details": "Origin and destination are required",
  "status": 400
}
```

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production (using Gunicorn)
```bash
gunicorn --bind 0.0.0.0:5000 main:app
```

### Cloud Run Deployment
Configuration in `.replit`:
```yaml
[deployment]
run = ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
deploymentTarget = "cloudrun"
```

## 📁 Project Structure

```
google-maps-route-api/
├── main.py             # Application logic and API endpoints
├── pyproject.toml      # Poetry configuration
├── .replit             # Replit/deployment configuration
├── README.md          # Documentation
└── .env.example       # Environment variable template
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|-----------|
| GOOGLE_MAPS_API_KEY | Google Maps API key | Yes |
| FLASK_ENV | Development/Production mode | No |
| PORT | API port (default: 5000) | No |

## 🔍 Error Handling

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid API key |
| 404 | Not Found - Location not found |
| 500 | Server Error - Google Maps API failure |

## 📊 Performance Considerations

- **Rate Limiting**
  - Google Maps API quotas apply
  - Implement client-side rate limiting
  - Consider caching frequent routes

- **Optimization**
  - Batch requests when possible
  - Implement request timeout handling
  - Use connection pooling

## 🛡️ Security

- API key protection
- Input validation
- HTTPS enforcement
- Request size limits
- Error message sanitization

## 🧪 Testing

Run the test suite:
```bash
poetry run pytest
```

Example test:
```python
def test_route_estimation():
    response = client.post('/get-route-estimation',
                         json={
                             'origin': 'Test Origin',
                             'destination': 'Test Destination'
                         })
    assert response.status_code == 200
    assert 'routes' in response.json
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📮 Support

For support:
- Open an issue in the GitHub repository
- Contact the maintainers
- Check the [Wiki](wiki) for additional documentation

## 🙏 Acknowledgments

- Google Maps Platform for their excellent API
- Flask community for the framework
- Contributors and users of this project