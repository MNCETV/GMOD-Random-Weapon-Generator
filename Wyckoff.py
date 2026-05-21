import random

categories = ["MNCE TV Script"]
hold_types = ["ar2", "pistol", "shotgun", "rpg", "physgun", "melee", "crossbow"]
ammo_types = ["Pistol", "357", "SMG1", "AR2", "Buckshot", "RPG_Round", "XBowBolt"]

v_models = [
"models/weapons/cstrike/c_pist_glock18.mdl",
    "models/weapons/cstrike/c_pist_p228.mdl",
    "models/weapons/cstrike/c_pist_deagle.mdl",
    "models/weapons/cstrike/c_pist_usp.mdl",          
    "models/weapons/cstrike/c_pist_usp.mdl",          
    "models/weapons/cstrike/c_pist_elite.mdl",
    "models/weapons/cstrike/c_pist_fiveseven.mdl",
    "models/weapons/cstrike/c_shot_m3super90.mdl",
    "models/weapons/cstrike/c_shot_xm1014.mdl",
    "models/weapons/cstrike/c_smg_p90.mdl",
    "models/weapons/cstrike/c_smg_mp5.mdl",
    "models/weapons/cstrike/c_smg_mac10.mdl",
    "models/weapons/cstrike/c_smg_ump45.mdl",
    "models/weapons/cstrike/c_mach_m249para.mdl",
    "models/weapons/cstrike/c_rif_galil.mdl",
    "models/weapons/cstrike/c_rif_ak47.mdl",
    "models/weapons/cstrike/c_rif_m4a1.mdl",          
    "models/weapons/cstrike/c_rif_m4a1.mdl",          
    "models/weapons/cstrike/c_rif_sg552.mdl",
    "models/weapons/cstrike/c_snip_awp.mdl",
    "models/weapons/cstrike/c_snip_scout.mdl",
    "models/weapons/cstrike/c_snip_g3sg1.mdl",
    "models/weapons/cstrike/c_snip_sg550.mdl",
    "models/weapons/cstrike/c_rif_famas.mdl",
    "models/weapons/cstrike/c_rif_aug.mdl",
    "models/weapons/c_irifle.mdl",
    "models/weapons/c_bugbait.mdl",
    "models/weapons/c_crossbow.mdl",
    "models/weapons/c_crowbar.mdl",
    "models/weapons/c_grenade.mdl",
    "models/weapons/c_physcannon.mdl",
    "models/weapons/c_pistol.mdl",
    "models/weapons/c_357.mdl",
    "models/weapons/c_rpg.mdl",
    "models/weapons/c_shotgun.mdl",
    "models/weapons/c_slam.mdl",
    "models/weapons/c_smg1.mdl",
    "models/weapons/c_stunstick.mdl",
    "models/weapons/c_toolgun.mdl",
    "models/weapons/c_superphyscannon.mdl",
    "models/weapons/c_medkit.mdl",
    "models/weapons/c_arms.mdl"
]
w_models = [
"models/weapons/w_irifle.mdl",
"models/weapons/w_bugbait.mdl",
"models/weapons/w_crossbow.mdl",
"models/weapons/w_crowbar.mdl",
"models/weapons/w_grenade.mdl",
"models/weapons/w_Physics.mdl",
"models/weapons/w_pistol.mdl",
"models/weapons/w_357.mdl",
"models/weapons/w_rocket_launcher.mdl",
"models/weapons/w_shotgun.mdl",
"models/weapons/w_slam.mdl",
"models/weapons/w_smg1.mdl",
"models/weapons/w_stunbaton.mdl",
"models/weapons/w_medkit.mdl",
"models/weapons/w_Physics.mdl",
"models/weapons/w_toolgun.mdl",
"models/weapons/w_pist_glock18.mdl",
    "models/weapons/w_pist_p228.mdl",
    "models/weapons/w_pist_deagle.mdl",
    "models/weapons/w_pist_usp.mdl",
    "models/weapons/w_pist_usp_silencer.mdl",
    "models/weapons/w_pist_elite.mdl",
    "models/weapons/w_pist_fiveseven.mdl",
    "models/weapons/w_shot_m3super90.mdl",
    "models/weapons/w_shot_xm1014.mdl",
    "models/weapons/w_smg_p90.mdl",
    "models/weapons/w_smg_mp5.mdl",
    "models/weapons/w_smg_mac10.mdl",
    "models/weapons/w_smg_ump45.mdl",
    "models/weapons/w_mach_m249para.mdl",
    "models/weapons/w_rif_galil.mdl",
    "models/weapons/w_rif_ak47.mdl",
    "models/weapons/w_rif_m4a1.mdl",
    "models/weapons/w_rif_m4a1_silencer.mdl",
    "models/weapons/w_rif_sg552.mdl",
    "models/weapons/w_snip_awp.mdl",
    "models/weapons/w_snip_scout.mdl",
    "models/weapons/w_snip_g3sg1.mdl",
    "models/weapons/w_snip_sg550.mdl",
    "models/weapons/w_rif_famas.mdl",
    "models/weapons/w_rif_aug.mdl",
    "models/weapons/w_irifle.mdl",
    "models/weapons/w_bugbait.mdl",
    "models/weapons/w_crossbow.mdl",
    "models/weapons/w_crowbar.mdl",
    "models/weapons/w_grenade.mdl",
    "models/weapons/w_physics.mdl",                  
    "models/weapons/w_pistol.mdl",
    "models/weapons/w_357.mdl",
    "models/weapons/w_rocket_launcher.mdl",          
    "models/weapons/w_shotgun.mdl",
    "models/weapons/w_slam.mdl",
    "models/weapons/w_smg1.mdl",
    "models/weapons/w_stunbaton.mdl"
]

shoot_sounds = [
    "AlyxEMP.Charge",
    "AlyxEMP.Discharge",
    "AlyxEMP.Stop",
    "BaseExplosionEffect.Sound",
    "BaseGrenade.BounceSound",
    "BaseGrenade.Explode",
    "BaseGrenade.StopSounds",
    "Grenade.Blip",
    "Grenade_Molotov.Detonate",
    "GrenadeBeam.HitSound",
    "GrenadeBottle.Detonate",
    "GrenadeBugBait.Splat",
    "GrenadeHomer.StopSounds",
    "GrenadePathfollower.StopSounds",
    "GrenadeScanner.StopSound",
    "TripwireGrenade.ShootRope",
    "WaterExplosionEffect.Sound",
    "WeaponFrag.Roll",
    "WeaponFrag.Throw",
    "Bullets.DefaultNearmiss",
    "Bullets.GunshipNearmiss",
    "Bullets.StriderNearmiss",
    "FX_RicochetSound.Ricochet",
    "Func_Tank.BeginUse",
    "FuncTank.Fire",
    "GenericNPC.GunSound",
    "Weapon_functank.Single",
    "Weapon_357.OpenLoader",
    "Weapon_357.Reload",
    "Weapon_357.RemoveLoader",
    "Weapon_357.ReplaceLoader",
    "Weapon_357.Single",
    "Weapon_357.Spin",
    "Weapon_AR2.Double",
    "Weapon_AR2.Empty",
    "Weapon_AR2.NPC_Double",
    "Weapon_AR2.NPC_Reload",
    "Weapon_AR2.NPC_Single",
    "Weapon_AR2.Reload",
    "Weapon_AR2.Reload_Push",
    "Weapon_AR2.Reload_Rotate",
    "Weapon_AR2.Single",
    "Weapon_AR2.Special1",
    "Weapon_AR2.Special2",
    "Weapon_IRifle.Empty",
    "Weapon_IRifle.Single",
    "Weapon_Crossbow.BoltElectrify",
    "Weapon_Crossbow.BoltFly",
    "Weapon_Crossbow.BoltHitBody",
    "Weapon_Crossbow.BoltHitWorld",
    "Weapon_Crossbow.BoltSkewer",
    "Weapon_Crossbow.Reload",
    "Weapon_Crossbow.Single",
    "Weapon_Crowbar.Melee_Hit",
    "Weapon_Crowbar.Melee_HitWorld",
    "Weapon_Crowbar.Single",
    "Weapon_StunStick.Activate",
    "Weapon_StunStick.Deactivate",
    "Weapon_StunStick.Melee_Hit",
    "Weapon_StunStick.Melee_HitWorld",
    "Weapon_StunStick.Melee_Miss",
    "Weapon_StunStick.Swing",
    "Weapon_Brickbat.Special1",
    "Weapon_Pistol.Burst",
    "Weapon_Pistol.Empty",
    "Weapon_Pistol.NPC_Reload",
    "Weapon_Pistol.NPC_Single",
    "Weapon_Pistol.Reload",
    "Weapon_Pistol.Single",
    "Weapon_Pistol.Special1",
    "Weapon_Pistol.Special2",
    "Weapon_Shotgun.Double",
    "Weapon_Shotgun.Empty",
    "Weapon_Shotgun.NPC_Reload",
    "Weapon_Shotgun.NPC_Single",
    "Weapon_Shotgun.Reload",
    "Weapon_Shotgun.Single",
    "Weapon_Shotgun.Special1",
    "Weapon_SMG1.Burst",
    "Weapon_SMG1.Double",
    "Weapon_SMG1.Empty",
    "Weapon_SMG1.NPC_Reload",
    "Weapon_SMG1.NPC_Single",
    "Weapon_SMG1.Reload",
    "Weapon_SMG1.Single",
    "Weapon_SMG1.Special1",
    "Weapon_SMG1.Special2",
    "Weapon_SniperRifle.NPC_Reload",
    "Weapon_SniperRifle.NPC_Single",
    "Weapon_SniperRifle.Reload",
    "Weapon_SniperRifle.Single",
    "Weapon_SniperRifle.Special1",
    "Weapon_SniperRifle.Special2",
    "Weapon_RPG.LaserOff",
    "Weapon_RPG.LaserOn",
    "Weapon_RPG.NPC_Single",
    "Weapon_RPG.Single",
    "Weapon_Mortar.Impact",
    "Weapon_Mortar.Incomming",
    "Weapon_Mortar.Single",
    "Weapon_PhysCannon.Charge",
    "Weapon_PhysCannon.CloseClaws",
    "Weapon_PhysCannon.Drop",
    "Weapon_PhysCannon.DryFire",
    "Weapon_PhysCannon.HoldSound",
    "Weapon_PhysCannon.Launch",
    "Weapon_PhysCannon.OpenClaws",
    "Weapon_PhysCannon.Pickup",
    "Weapon_PhysCannon.TooHeavy",
    "Weapon_MegaPhysCannon.Charge",
    "Weapon_MegaPhysCannon.ChargeZap",
    "Weapon_MegaPhysCannon.Drop",
    "Weapon_MegaPhysCannon.DryFire",
    "Weapon_MegaPhysCannon.HoldSound",
    "Weapon_MegaPhysCannon.Launch",
    "Weapon_MegaPhysCannon.Pickup",
    "Weapon_Physgun.HeavyObject",
    "Weapon_Physgun.LightObject",
    "Weapon_Physgun.LockedOn",
    "Weapon_Physgun.Off",
    "Weapon_Physgun.On",
    "Weapon_Physgun.Scanning",
    "Weapon_Physgun.Special1",
    "Weapon_Binoculars.Reload",
    "Weapon_Binoculars.Special1",
    "Weapon_Binoculars.Special2",
    "Weapon_Bugbait.Splat",
    "Weapon_CombineGuard.Special1",
    "Weapon_Extinguisher.Double",
    "Weapon_Extinguisher.Empty",
    "Weapon_Extinguisher.NPC_Double",
    "Weapon_Extinguisher.NPC_Reload",
    "Weapon_Extinguisher.NPC_Single",
    "Weapon_Extinguisher.Reload",
    "Weapon_Extinguisher.Single",
    "Weapon_Extinguisher.Special1",
    "Weapon_FlareGun.Burn",
    "Weapon_FlareGun.Reload",
    "Weapon_FlareGun.Single",
    "Weapon_Gauss.ChargeLoop"
]

prop_models = [
    "models/props_junk/watermelon01.mdl", "models/props_junk/metal_paintcan001a.mdl",
    "models/props_junk/garbage_coffeemug001a.mdl", "models/props_c17/FurnitureCouch001a.mdl",
    "models/lamps/torch.mdl","models/props_c17/FurnitureBathtub001a.mdl","models/props_c17/fountain_01.mdl",
    "models/props_c17/oildrum001_explosive.mdl",
    "models/props_c17/chair_stool01a.mdl",
    "models/props_c17/furniturecouch001a.mdl",
    "models/props_c17/furniturecouch002a.mdl",
    "models/props_c17/furnituredresser001a.mdl",
    "models/props_c17/furniturestove001a.mdl",
    "models/props_c17/furnituretable001a.mdl",
    "models/props_c17/furnituretable002a.mdl",
    "models/props_c17/furniturechair001a.mdl",
    "models/props_trainstation/trashcan_indoor001a.mdl",
    "models/props_junk/sawblade001a.mdl",
    "models/props_c17/metalPot001a.mdl",
    "models/props_c17/metalPot002a.mdl",
    "models/props_c17/lockers001a.mdl",
    "models/props_c17/display_cooler01a.mdl",
    "models/props_c17/concrete_barrier001a.mdl",
    "models/props_c17/fence01a.mdl",
    "models/props_c17/statue_horse.mdl",
    "models/props_c17/playgroundtick-tack-toe_block01a.mdl",
    "models/props_c17/oildrum001_explosive.mdl",
    "models/props_c17/trappropeller_blade.mdl",
    "models/props_c17/trappropeller_engine.mdl"
]

proj_entities = ["rpg_missile", "grenade_ar2", "npc_grenade_frag", "cross_bolt","prop_combine_ball","npc_tripmine","npc_satchel","grenade_helicopter","hunter_flechette",
"combine_mine"
]

wep_id = random.randint(100000, 999999)
name = f"Cursed SWEP #{wep_id}"
category = random.choice(categories)
vmodel = random.choice(v_models)
wmodel = random.choice(w_models)
use_hands = 'true' if random.random() > 0.3 else 'false'
clip = random.randint(1, 200)
is_auto = 'true' if random.random() > 0.2 else 'false'
ammo = random.choice(ammo_types)
delay = round(random.uniform(0.01, 1.5), 3)
hold_type = random.choice(hold_types)
shoot_sound = random.choice(shoot_sounds)
recoil = round(random.uniform(0.1, 30.0), 2)
wep_types = ['hitscan', 'prop', 'projectile']
wep_type = random.choice(wep_types)
damage = random.randint(1, 500)
spread = round(random.uniform(0.0, 0.5), 3)
prop_mdl = random.choice(prop_models)
proj_ent = random.choice(proj_entities)

lua_code = f"""AddCSLuaFile()
SWEP.PrintName = "{name}"
SWEP.Category = "{category}"
SWEP.Spawnable = true
SWEP.AdminOnly = false

SWEP.Base = "weapon_base"

SWEP.ViewModel = "{vmodel}"
SWEP.WorldModel = "{wmodel}"
SWEP.UseHands = {use_hands}

SWEP.Primary.ClipSize = {clip}
SWEP.Primary.DefaultClip = {clip * 3}
SWEP.Primary.Automatic = {is_auto}
SWEP.Primary.Ammo = "{ammo}"
SWEP.Primary.Delay = {delay}

SWEP.Secondary.ClipSize = -1
SWEP.Secondary.DefaultClip = -1
SWEP.Secondary.Automatic = false
SWEP.Secondary.Ammo = "none"

function SWEP:Initialize()
    self:SetHoldType("{hold_type}")
end

function SWEP:PrimaryAttack()
    if not self:CanPrimaryAttack() then return end

    local ply = self:GetOwner()
    if not IsValid(ply) then return end

    self:EmitSound("{shoot_sound}")
    self:TakePrimaryAmmo(1)
    self:SetNextPrimaryFire(CurTime() + self.Primary.Delay)
    
    self:ShootEffects()

    ply:ViewPunch(Angle(-{recoil}, math.Rand(-1, 1), 0))
"""

if wep_type == 'hitscan':
    lua_code += f"""    self:ShootBullet({damage}, 1, {spread})
end
"""
else:
    ent_class = 'prop_physics' if wep_type == 'prop' else proj_ent
    model_setup = f'ent:SetModel("{prop_mdl}")' if wep_type == 'prop' else '-- Standard Projectile Initialization'
    
    lua_code += f"""    if SERVER then
        local ent = ents.Create("{ent_class}")
        if IsValid(ent) then
            {model_setup}
            local spawnPos = ply:GetShootPos() + ply:GetAimVector() * 32
            ent:SetPos(spawnPos)
            ent:SetAngles(ply:EyeAngles())
            ent:SetOwner(ply)
            ent:Spawn()
            ent:Activate()
            
            local phys = ent:GetPhysicsObject()
            if IsValid(phys) then
                phys:Wake()
                local aimDir = ply:GetAimVector()
                aimDir = aimDir + VectorRand() * ({spread} / 2)
                phys:SetVelocity(aimDir * 2000)
            end
        end
    end
end
"""

output_file = f"weapon_{wep_id}.lua"
with open(output_file, 'w') as fh:
    fh.write(lua_code)

print(f"{wep_type} '{output_file}'!")
