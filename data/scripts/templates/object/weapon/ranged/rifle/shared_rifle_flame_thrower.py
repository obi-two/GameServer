#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Weapon()

	result.template = "object/weapon/ranged/rifle/shared_rifle_flame_thrower.iff"
	result.attribute_template_id = 10
	result.stfName("weapon_name","rifle_flame_thrower")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result