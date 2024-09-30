from etl import SepaETL, Configs, SepaExtract, Transform


if __name__ == "__main__":
    configs = [Configs.ComerciosConfig]
    # configs = (Configs.ComerciosConfig, Configs.ProductosConfig, Configs.SucursalesConfig)
    for config in configs:
        lines = SepaETL.process(config, SepaExtract, Transform)
        SepaETL.load(lines, config)