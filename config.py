import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Configurações de e-mail via SendGrid ---
    SENDGRID_API_KEY = "SG.sua_chave_aqui"  # substitua pela sua chave real
    FROM_EMAIL = "flaskaulasweb@zohomail.com"
    TO_EMAIL = "seu_email_institucional@exemplo.com"  # substitua pelo seu

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'testing': TestingConfig,
    'default': Config
}
