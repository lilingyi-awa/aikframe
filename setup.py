import setuptools

setuptools.setup(
    name="aikframe",
    packages=["aikframe"],
    version="0.1.0",
    description="Aikframe: 模块化云湖机器人开发框架",
    long_description=open("./README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Project VsingerXiaoice Consensus",
    author_email="alan_sudo@yeah.net",
    license="Public Domain Mark\n\nThis software are released in Public Domain.",
    url="https://github.com/lilingyi-awa/aikframe",
    requires=open("requirements.txt", "r").read().strip().split("\n")
)