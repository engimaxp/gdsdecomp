#ifndef VARIANT_WRITER_COMPAT_H
#define VARIANT_WRITER_COMPAT_H

#include "core/io/file_access.h"
#include "core/io/resource.h"
#include "core/variant/variant.h"
#include "core/variant/variant_parser.h"

class VariantParserCompat : VariantParser {
	static Error fake_parse_object(VariantParser::Token &token, Variant &value, VariantParser::Stream *p_stream, int &line, String &r_err_str, VariantParser::ResourceParser *p_res_parser);

public:
	static Error parse_tag(VariantParser::Stream *p_stream, int &line, String &r_err_str, Tag &r_tag, VariantParser::ResourceParser *p_res_parser = nullptr, bool p_simple_tag = false);
	static Error parse_tag_assign_eof(VariantParser::Stream *p_stream, int &line, String &r_err_str, Tag &r_tag, String &r_assign, Variant &r_value, VariantParser::ResourceParser *p_res_parser = nullptr, bool p_simple_tag = false);
};

class VariantWriterCompat {
public:
	typedef Error (*StoreStringFunc)(void *ud, const String &p_string);
	typedef String (*EncodeResourceFunc)(void *ud, const Ref<Resource> &p_resource);
	static Error write_compat(const Variant &p_variant, const uint32_t ver_major, StoreStringFunc p_store_string_func, void *p_store_string_ud, EncodeResourceFunc p_encode_res_func, void *p_encode_res_ud);
	static Error write_to_string(const Variant &p_variant, String &r_string, const uint32_t ver_major, EncodeResourceFunc p_encode_res_func = nullptr, void *p_encode_res_ud = nullptr);
};

#endif // VARIANT_WRITER_COMPAT_H
