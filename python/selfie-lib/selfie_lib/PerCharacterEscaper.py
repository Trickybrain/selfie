class PerCharacterEscaper:
    def __init__(self, escape_code_point, escaped_code_points, escaped_by_code_points):
        self.escape_code_point = escape_code_point
        self.escaped_code_points = escaped_code_points
        self.escaped_by_code_points = escaped_by_code_points

    @staticmethod
    def _first_offset_needing_escape(
        input_string, escaped_code_points, escape_code_point=None
    ):
        length = len(input_string)
        for offset in range(length):
            codepoint = ord(input_string[offset])
            if escape_code_point is not None and codepoint == escape_code_point:
                return offset
            if codepoint in escaped_code_points:
                return offset
        return -1

    def escape(self, input_string):
        no_escapes = self._first_offset_needing_escape(
            input_string, self.escaped_code_points
        )
        if no_escapes == -1:
            return input_string
        else:
            result = []
            result.append(input_string[:no_escapes])
            for char in input_string[no_escapes:]:
                codepoint = ord(char)
                if codepoint in self.escaped_code_points:
                    idx = self.escaped_code_points.index(codepoint)
                    result.append(chr(self.escape_code_point))
                    result.append(chr(self.escaped_by_code_points[idx]))
                else:
                    result.append(char)
            return "".join(result)

    def unescape(self, input_string):
        if input_string.endswith(
            chr(self.escape_code_point)
        ) and not input_string.endswith(chr(self.escape_code_point) * 2):
            raise ValueError(
                "Escape character '{}' can't be the last character in a string.".format(
                    chr(self.escape_code_point)
                )
            )

        no_escapes = self._first_offset_needing_escape(
            input_string, [self.escape_code_point], self.escape_code_point
        )
        if no_escapes == -1:
            return input_string
        else:
            result = []
            result.append(input_string[:no_escapes])
            skip_next = False
            for i in range(no_escapes, len(input_string)):
                if skip_next:
                    skip_next = False
                    continue
                codepoint = ord(input_string[i])
                if codepoint == self.escape_code_point and (i + 1) < len(input_string):
                    next_codepoint = ord(input_string[i + 1])
                    if next_codepoint in self.escaped_by_code_points:
                        idx = self.escaped_by_code_points.index(next_codepoint)
                        result.append(chr(self.escaped_code_points[idx]))
                        skip_next = True
                    else:
                        result.append(input_string[i + 1])
                        skip_next = True
                else:
                    result.append(chr(codepoint))
            return "".join(result)

    @classmethod
    def self_escape(cls, escape_policy):
        code_points = [ord(c) for c in escape_policy]
        escape_code_point = code_points[0]
        return cls(escape_code_point, code_points, code_points)

    @classmethod
    def specified_escape(cls, escape_policy):
        code_points = [ord(c) for c in escape_policy]
        if len(code_points) % 2 != 0:
            raise ValueError(
                "Escape policy string must have an even number of characters."
            )
        escape_code_point = code_points[0]
        escaped_code_points = code_points[0::2]
        escaped_by_code_points = code_points[1::2]
        return cls(escape_code_point, escaped_code_points, escaped_by_code_points)
