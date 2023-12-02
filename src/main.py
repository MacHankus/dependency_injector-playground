from container import Container


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=["fake_db_session"])