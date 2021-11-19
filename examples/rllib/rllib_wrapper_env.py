from environments.track_env import TrackEnvWind


class RllibWrapperEnv(TrackEnvWind):
    def __init__(self, config):

        if config["evaluation"]:
            seed = config["seed_value"]
        else:
            seed = config["seed_value"] + config.worker_index + config.num_workers + config.vector_index

        config["seed_value"] = seed
        super().__init__(**config)

        self.seed(seed)

