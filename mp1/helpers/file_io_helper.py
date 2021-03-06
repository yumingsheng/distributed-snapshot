import os

def save_snapshot_state(pid, snapshot_id, state):
    """state is a tuple of (logical, vector, asset) where logical is an int,
    vector is a list, state is [widget, money]"""

    logical = state[0]
    vector = " ".join(str(i) for i in state[1])
    asset = state[2]
    content = "id {} : snapshot {} : logical {} : vector {} : money {} : widgets {}\n".format(
        pid, snapshot_id, logical, vector, asset[1], asset[0]
    )

    filename = os.path.dirname(os.path.realpath(__file__)) + "/../../snapshots/snapshot." + str(pid)
    with open(filename, "a") as f:
        f.write(content)

def save_snapshot_channel(pid, snapshot_id, channel, channel_id):
    content = ''
    for entry in channel['data']:
        type = entry[0]
        print("type: ", type)

        asset_type = ''
        if type == 1: # 'send_widget'
            print("type send_widget")
            asset_type = 'widget'
        else:
            asset_type = 'money'

        amount = entry[1]
        logical_timestamp = entry[2]
        vector_timestamp = entry[3:]

        vector_timestamp_str = " ".join(str(i) for i in entry[3:])

        content = content + "id {} : snapshot {} : logical {} : vector {} : message {} to {} : {} {}\n".format(
            pid, snapshot_id, logical_timestamp, vector_timestamp_str, channel_id, pid, asset_type, amount
        )

    snapshot_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../snapshots/"
    filename = snapshot_dir + "snapshot." + str(pid)
    with open(filename, "a") as f:
        f.write(content)

def delete_snapshots():
    snapshot_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../snapshots/"
    try:
        file_list = [f for f in os.listdir(snapshot_dir) if f.startswith("snapshot.")]
        for f in file_list:
            os.remove(snapshot_dir + f)
    except:
        print("file IO exception")
        pass
