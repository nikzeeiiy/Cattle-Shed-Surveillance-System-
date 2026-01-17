import math

def calculate_angle(kp1, kp2, kp3):
    """
    Calculate the angle (in degrees) between three keypoints.
    """
    vec1 = (kp1[0] - kp2[0], kp1[1] - kp2[1])
    vec2 = (kp3[0] - kp2[0], kp3[1] - kp2[1])

    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    magnitude1 = math.sqrt(vec1[0]**2 + vec1[1]**2)
    magnitude2 = math.sqrt(vec2[0]**2 + vec2[1]**2)
    angle = math.acos(dot_product / (magnitude1 * magnitude2))

    return math.degrees(angle)

def detect_stomping(keypoints):
    """
    Detect if the cow is stomping based on keypoint angles.
    """
    # Extract relevant keypoint coordinates
    neck = keypoints[3]
    left_shoulder = keypoints[4]
    right_shoulder = keypoints[7]
    left_knee = keypoints[12]
    right_knee = keypoints[15]
    left_back_paw = keypoints[13]
    right_back_paw = keypoints[16]

    # Calculate angles
    left_leg_angle = calculate_angle(left_knee, left_shoulder, neck)
    right_leg_angle = calculate_angle(right_knee, right_shoulder, neck)
    left_paw_angle = calculate_angle(left_back_paw, left_knee, left_shoulder)
    right_paw_angle = calculate_angle(right_back_paw, right_knee, right_shoulder)

    # Set stomping angle thresholds (you may need to adjust these based on your data)
    stomping_leg_angle_min = 60
    stomping_leg_angle_max = 120
    stomping_paw_angle_min = 90
    stomping_paw_angle_max = 180

    # Check if angles fall within stomping range
    is_stomping = (
        (left_leg_angle > stomping_leg_angle_min and left_leg_angle < stomping_leg_angle_max) and
        (right_leg_angle > stomping_leg_angle_min and right_leg_angle < stomping_leg_angle_max) and
        (left_paw_angle > stomping_paw_angle_min and left_paw_angle < stomping_paw_angle_max) and
        (right_paw_angle > stomping_paw_angle_min and right_paw_angle < stomping_paw_angle_max)
    )

    return is_stomping

# Usage example
keypoints = [(10, 20), (30, 40), (50, 60), (70, 80), (90, 100), (110, 120), (130, 140), (150, 160), (170, 180), (190, 200), (210, 220), (230, 240), (250, 260), (270, 280), (290, 300), (310, 320), (330, 340)]

if detect_stomping(keypoints):
    print("Cow is stomping!")
else:
    print("Cow is not stomping.")