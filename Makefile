patch-p: patch install publish push
minor-p: minor install publish push
major-p: major install publish push

install:
	uv sync

publish:
	uv build && uvx twine upload dist/*

patch:
	uvx bump2version patch

minor:
	uvx bump2version minor

major:
	uvx bump2version major

push:
	git push origin master


.PHONE: *
