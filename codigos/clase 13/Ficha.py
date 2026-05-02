class Ficha:
    def __init__(self, valor):
        self._valor = valor
        self._visible = False
        self._encontrada = False

    @property
    def valor(self):
        return self._valor

    @property
    def visible(self):
        return self._visible

    @property
    def encontrada(self):
        return self._encontrada

    def voltear(self):
        """Cambia entre boca arriba y boca abajo."""
        self._visible = not self._visible

    def marcar_pareja(self):
        """La ficha quedó encontrada: visible para siempre."""
        self._encontrada = True
        self._visible    = True

    def __str__(self):
        return self._valor if self._visible else "?"
