import psycopg2


class DBWriter:

    def __init__(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="autonomy",
            user="postgres",
            password="postgres",
            port="5432"
        )

        self.cursor = self.conn.cursor()

    def insert_test_run(
            self,
            software_version,
            scenario_name,
            weather):

        query = """
        INSERT INTO test_run
        (
            software_version,
            scenario_name,
            weather,
            execution_date
        )
        VALUES (%s,%s,%s,NOW())
        RETURNING run_id;
        """

        self.cursor.execute(
            query,
            (
                software_version,
                scenario_name,
                weather
            )
        )

        result = self.cursor.fetchone()

        if result is None:
            raise Exception(
                "Failed to return run_id."
            )

        run_id = result[0]

        self.conn.commit()

        return run_id

    def insert_perception_metrics(
            self,
            run_id,
            precision,
            recall,
            f1,
            miss_rate):

        self.cursor.execute(
            """
            INSERT INTO perception_metrics(
                run_id,
                precision,
                recall,
                f1_score,
                missed_pedestrian_rate
            )
            VALUES(%s,%s,%s,%s,%s)
            """,
            (
                run_id,
                precision,
                recall,
                f1,
                miss_rate
            )
        )

        self.conn.commit()

    def insert_planning_metrics(
            self,
            run_id,
            lane_error,
            min_ttc,
            collision_count):

        self.cursor.execute(
            """
            INSERT INTO planning_metrics(
                run_id,
                lane_error,
                min_ttc,
                collision_count
            )
            VALUES(%s,%s,%s,%s)
            """,
            (
                run_id,
                lane_error,
                min_ttc,
                collision_count
            )
        )

        self.conn.commit()

    def insert_control_metrics(
            self,
            run_id,
            tracking_error,
            avg_acceleration,
            avg_jerk
    ):

        self.cursor.execute(
            """
            INSERT INTO control_metrics(
                run_id,
                path_tracking_error,
                avg_acceleration,
                avg_jerk
            )
            VALUES(%s,%s,%s,%s)
            """,
            (
                run_id,
                tracking_error,
                avg_acceleration,
                avg_jerk
            )
        )

        self.conn.commit()

    def insert_release_decision(
            self,
            run_id,
            score,
            risk,
            decision):

        self.cursor.execute(
            """
            INSERT INTO release_decision(
                run_id,
                safety_score,
                risk_score,
                decision
            )
            VALUES(%s,%s,%s,%s)
            """,
            (
                run_id,
                score,
                risk,
                decision
            )
        )

        self.conn.commit()

    def close(self):

        self.cursor.close()
        self.conn.close()