import facebook
token='EAAJ0HTX3Xo8BAEe2l5tSgPMigCo1jMcno5kjE3YZA5RKRX3rliKxg3YpfIkkyJGy2vZC8r4AXVHFqJPIXkJZBn7J1EvmWG2ThG1tfBaRxAV2GF4oQXDNG2PHLGfvO5XjsTtNtwei7YfX4N6uhcfCAXaLv7zSh3qETrvrjObxqwZBp9xWo5ZBnon7O5FwB8lPFTc06NPAbZBwZDZD'

fb=facebook.GraphAPI(access_token=token)

fb.put_object(parent_object='me', connection_name='feed',message='hey this is my first app')


