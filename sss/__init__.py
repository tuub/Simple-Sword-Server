from .info import __version__, __author__, __license__

from .core import Auth, AuthException, Authenticator, DeleteRequest, DeleteResponse, DepositRequest, DepositResponse, EntryDocument, SDCollection, SWORDRequest, ServiceDocument, Statement, SwordError, SwordServer, WebUI
from .config import Configuration, SSS_CONFIG_FILE
from .spec import Errors, HttpHeaders, Namespaces

from . import ingesters_disseminators
from . import negotiator
from . import repository
