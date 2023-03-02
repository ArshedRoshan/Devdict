from django.core.mail import EmailMessage
import jwt
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# class Util:
#     @staticmethod
#     def send_email(data):
#         email = EmailMessage(subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
#         email.send()
        
        
        
 
# def send_verification_email(user_data):
#   # Generate a JWT token with a user id claim
#   token = jwt.encode({'user_id': user_data['id']}, 'secret', algorithm='HS256')
  
#   # Encode the token as a URL-safe base64 string
#   token = urlsafe_base64_encode(force_bytes(token)).decode()
  
#   # Build the verification link
#   verification_link = f'http://example.com/verify-email?token={token}'
  
#   # Send the email
#   send_mail(
#     'Verify Your Email',
#     f'Click the link to verify your email: {verification_link}',
#     'noreply@example.com',
#     [user_data['email']],
#     fail_silently=False,
#   )