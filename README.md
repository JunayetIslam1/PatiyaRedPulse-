# Patiya RedPulse - Blood Donor Directory

A simple, fast, and trustworthy blood donation platform for Patiya, Chattogram, Bangladesh.

## 🎯 Objective

Create a direct connection system between blood seekers and donors without any middleman complexity. This platform is designed for emergency use with mobile-first approach.

## ✨ Features

### For Blood Seekers
- **Search donors** by blood group, district, and upazila
- **View donor eligibility** status (auto-calculated 90-day rule)
- **Direct calling** with one-click tel: links
- **Submit blood requests** for emergency situations

### For Donors
- **Simple registration** with minimal required fields
- **Automatic eligibility tracking** (90-day donation gap)
- **Availability status control** (Available/Not Available)
- **Profile management** with update capabilities

### For Admins
- **Dashboard statistics** with real-time counts
- **Donor management** (block/unblock functionality)
- **Request management** (delete fake/spam requests)
- **Django admin panel** for full database access

## 🛠️ Technology Stack

- **Backend:** Django 4.2+ (Python)
- **Database:** SQLite3 (production-ready)
- **Frontend:** Bootstrap 5 + Custom CSS
- **Authentication:** Django built-in system
- **Security:** CSRF protection, password hashing

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone/Download the project**
   ```bash
   cd patiya_redpulse
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Settings to Customize

1. **Secret Key** - Change `SECRET_KEY` in `settings.py` for production
2. **Debug Mode** - Set `DEBUG = False` in production
3. **Allowed Hosts** - Add your domain/IP to `ALLOWED_HOSTS`
4. **Database** - Currently uses SQLite3 (suitable for this use case)

### Creating an Admin User

After running `python manage.py createsuperuser`, you can:
1. Login to Django admin at `/admin/`
2. Access the custom admin panel at `/admin-panel/`
3. Manage donors and requests from the dashboard

## 📱 Mobile-First Design

The platform is optimized for:
- Low-end Android phones
- Slow internet connections
- Touch interfaces
- Small screens
- Emergency situations

## 🔐 Security Features

- Django authentication system
- Password hashing (PBKDF2)
- CSRF protection on all forms
- Server-side validation
- No raw SQL queries
- XSS protection

## 🩸 Donor Eligibility Logic

The system automatically calculates:
- Days since last donation
- Eligibility status (90-day minimum gap)
- Visual indicators for eligible/not eligible donors

**Eligible Donors:** Green badge with checkmark
**Not Eligible:** Yellow badge with countdown days

## 📞 Direct Contact System

- Phone numbers are publicly visible
- One-click calling using `tel:` protocol
- No OTP or SMS verification
- Direct connection between seeker and donor

## 🏥 Emergency Handling

- Emergency requests highlighted in red
- Pulsing animation for visual attention
- Emergency badge on request cards
- Admin dashboard shows emergency count

## 🌍 Location Coverage

Designed specifically for:
- **Country:** Bangladesh
- **Primary Area:** Patiya, Chattogram
- **District/Upazila system** for precise location

## 📊 Database Schema

### Donor Model
- User account (Django User)
- Personal information (name, age, gender)
- Blood group and location
- Last donation date and eligibility
- Contact information (mobile required, email optional)

### BloodRequest Model
- Patient information
- Required blood group and bags
- Hospital details
- Emergency level and required date
- Contact information

## 🚀 Production Deployment

For production deployment:

1. **Security**
   - Change SECRET_KEY
   - Set DEBUG = False
   - Configure ALLOWED_HOSTS
   - Use HTTPS

2. **Performance**
   - Use a production web server (Gunicorn, uWSGI)
   - Configure static file serving
   - Set up database backups

3. **Monitoring**
   - Set up error logging
   - Monitor server resources
   - Regular database maintenance

## 🤝 Contributing

This is a humanitarian project. To contribute:
1. Test the platform thoroughly
2. Report bugs and issues
3. Suggest improvements
4. Help spread awareness
5. Register as a donor

## ⚠️ Important Disclaimers

1. **Medical Responsibility:** This platform only connects donors and seekers. Medical verification is the responsibility of the parties involved.

2. **Identity Verification:** Always verify donor identity and blood compatibility before transfusion.

3. **Emergency Situations:** For life-threatening emergencies, contact the nearest hospital immediately.

4. **Data Privacy:** Phone numbers are publicly visible. Register only if you consent to this.

5. **Humanitarian Use:** This platform is for genuine blood donation needs only.

## 📞 Support

For technical support or questions:
- Check the admin panel for user management
- Review Django admin for database access
- Monitor the platform for fake/spam content

## 📄 License

This project is created for humanitarian purposes. Use it to save lives in Patiya and beyond.

---

**Built with ❤️ for the people of Patiya, Chattogram.**

*Saving lives through direct connection.*