import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Error, Text, Other, \
     Comment, Operator, Keyword, Name, String, Number, Generic, Punctuation


class FancyLexer(RegexLexer):
    """
    Pygments Lexer For `Fancy <http://www.fancy-lang.org/>`.

    Fancy is a self-hosted, pure object-oriented, dynamic,
    class-based, concurrent general-purpose programming language
    running on Rubinius, the Ruby VM.

    **New in Pygments 1.5**
    """

    name = 'Fancy'
    filenames = ['*.fy', '*.fancypack']
    aliases = ['fancy', 'fy']
    mimetypes = ['text/x-fancysrc']

    tokens = {
        # copied from PerlLexer:
        'balanced-regex': [
            (r'/(\\\\|\\/|[^/])*/[egimosx]*', String.Regex, '#pop'),
            (r'!(\\\\|\\!|[^!])*![egimosx]*', String.Regex, '#pop'),
            (r'\\(\\\\|[^\\])*\\[egimosx]*', String.Regex, '#pop'),
            (r'{(\\\\|\\}|[^}])*}[egimosx]*', String.Regex, '#pop'),
            (r'<(\\\\|\\>|[^>])*>[egimosx]*', String.Regex, '#pop'),
            (r'\[(\\\\|\\\]|[^\]])*\][egimosx]*', String.Regex, '#pop'),
            (r'\((\\\\|\\\)|[^\)])*\)[egimosx]*', String.Regex, '#pop'),
            (r'@(\\\\|\\\@|[^\@])*@[egimosx]*', String.Regex, '#pop'),
            (r'%(\\\\|\\\%|[^\%])*%[egimosx]*', String.Regex, '#pop'),
            (r'\$(\\\\|\\\$|[^\$])*\$[egimosx]*', String.Regex, '#pop'),
        ],
        'root': [
            (r'\n', Text),
            (r'\s+', Text),

            # balanced delimiters (copied from PerlLexer):
            (r's{(\\\\|\\}|[^}])*}\s*', String.Regex, 'balanced-regex'),
            (r's<(\\\\|\\>|[^>])*>\s*', String.Regex, 'balanced-regex'),
            (r's\[(\\\\|\\\]|[^\]])*\]\s*', String.Regex, 'balanced-regex'),
            (r's\((\\\\|\\\)|[^\)])*\)\s*', String.Regex, 'balanced-regex'),
            (r'm?/(\\\\|\\/|[^/\n])*/[gcimosx]*', String.Regex),
            (r'm(?=[/!\\{<\[\(@%\$])', String.Regex, 'balanced-regex'),

            # Comments
            (r'#(.*?)\n', Comment.Single),
            # Symbols
            (r'\'[\S]*', String.Symbol),
            # DoubleQuotedString
            (r'"(\\\\|\\"|[^"])*"', String),
            # Multi-line DoubleQuotedString
            (r'"""(\\\\|\\"|[^"])*"""', String),
            # keywords
            (r'(def|class|try|catch|finally|retry|return|return_local|match|case|->|=>)\b', Keyword),
            # Operators
            (r'[-+*/~,<>=&!?%^\[\]]+', Operator),
            # constants
            (r'(self|super|nil|false|true)\b', Name.Constant),
            (r'[(){};,/?\|:\\]', Punctuation),
            # names
            ('(Object|Array|Hash|Directory|File|Class|String|Number|Enumerable|FancyEnumerable|Block|TrueClass|NilClass|FalseClass|Tuple|Symbol|Stack|Set|FancySpec|Method|Package|Range)\b', Name.Builtin),
            (r'[a-zA-Z]([a-zA-Z0-9_]|[-+?!=*/^><%])*:', Name.Function),
            ('[A-Z][a-zA-Z0-9_]*', Name.Constant),
            ('@[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable.Instance),
            ('@@[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable.Class),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
            # numbers
            (r'(0(o|O)?[0-7]+(?:_[0-7]+)*)(\s*)([/?])?',
             bygroups(Number.Oct, Text, Operator)),
            (r'(0(x|X)[0-9A-Fa-f]+(?:_[0-9A-Fa-f]+)*)(\s*)([/?])?',
             bygroups(Number.Hex, Text, Operator)),
            (r'(0(b|B)[01]+(?:_[01]+)*)(\s*)([/?])?',
             bygroups(Number.Bin, Text, Operator)),
            (r'([\d]+(?:_\d+)*)(\s*)([/?])?',
             bygroups(Number.Integer, Text, Operator)),
            (r'(\d+\.?\d*|\d*\.\d+)([eE][+-]?[0-9]+)?', Number.Float),
            (r'\d+', Number.Integer)
        ]
    }
