int RawToDecRPId(int raw)
{
	int arm = (int)(raw / 2^24) % 2;
	int st = (int)(raw / 2^22) % 4;
	int rp = (int)(raw / 2^19) % 8;

	return arm*100 + st*10 + rp;
}

//---------------------------------------------------------------------------------------------------------------------

int RawToDecSensorId(int raw)
{
	int subdet = (int)(raw / 2^25) % 8;
	int arm = (int)(raw / 2^24) % 2;
	int st = (int)(raw / 2^22) % 4;
	int rp = (int)(raw / 2^19) % 8;

	int plane = -1;

	// strips
	if (subdet == 3)
		plane = (int)(raw / 2^15) % 16;

	// pixels
	if (subdet == 4)
		plane = (int)(raw / 2^16) % 8;

	if (plane < 0)
		write("ERROR in RawToDecSensorId > plane < 0.");

	return arm*1000 + st*100 + rp*10 + plane;
}

//---------------------------------------------------------------------------------------------------------------------

string SensorTypeFromRawId(int raw)
{
	int subdet = (int)(raw / 2^25) % 8;
	int arm = (int)(raw / 2^24) % 2;
	int st = (int)(raw / 2^22) % 4;
	int rp = (int)(raw / 2^19) % 8;

	// pixels
	if (subdet == 4)
		return "pixels";

	// strips
	if (subdet == 3)
	{
		int plane = (int)(raw / 2^15) % 16;
		if (plane % 2 == 0)
			return "strips, V";
		else
			return "strips, U";
	}

	return "unknown";
}

//---------------------------------------------------------------------------------------------------------------------

string RPName(int rp)
{
	string a = (quotient(rp, 100) >= 1) ? "56" : "45";
	string s = (quotient(rp, 10) % 10 == 2) ? "220" : "210";
	string u = ((rp % 10) > 2) ? "far" : "near";
	int R = rp % 10;
	string r = "";
	if (R == 0 || R == 4) r = "top";
	if (R == 1 || R == 5) r = "bot";
	if (R == 2 || R == 3) r = "hor";
	
	return a+"-"+s+"-"+u+"-"+r;
}

//---------------------------------------------------------------------------------------------------------------------

struct Alignment
{
	string sensorType[];

	real shr[], shr_e[];
	real shx[], shx_e[];
	real shy[], shy_e[];
	real shz[], shz_e[];
	real rotz[], rotz_e[];

	real rp_shx[], rp_shx_e[];
	real rp_shy[], rp_shy_e[];
	real rp_rotz[], rp_rotz_e[];
};

//---------------------------------------------------------------------------------------------------------------------

int ParseXML(string filename, Alignment a)
{
	a.sensorType.delete();

	a.shr.delete();
	a.shr_e.delete();
	a.rotz.delete();
	a.rotz_e.delete();
	
	a.rp_shx.delete();
	a.rp_shx_e.delete();
	a.rp_shy.delete();
	a.rp_shy_e.delete();
	a.rp_rotz.delete();
	a.rp_rotz_e.delete();

	file f = input(filename, false);
	if (error(f))
		return 1;

	while (!eof(f))
	{
		string line = f;
		string[] bits = split(line, "\"");
		//write(line);

		bool det_node = (find(line, "<det") >= 0);
		bool rp_node = (find(line, "<rp") >= 0);
		if (!det_node && !rp_node)
			continue;

		int id_raw = -1;
		real sh_r = 0, sh_r_e = 0, rot_z = 0, rot_z_e = 0;
		real sh_x = 0, sh_x_e = 0, sh_y = 0, sh_y_e = 0;
		real sh_z = 0, sh_z_e = 0;

		for (int j = 0; j < bits.length; ++j)
		{
			//write("> ", bits[j]);
			if (find(bits[j], "id=") >= 0) id_raw = (int) bits[++j];
			if (find(bits[j], "sh_r=") >= 0) sh_r = (real) bits[++j];
			if (find(bits[j], "sh_r_e=") >= 0) sh_r_e = (real) bits[++j];
			if (find(bits[j], "sh_x=") >= 0) sh_x = (real) bits[++j];
			if (find(bits[j], "sh_x_e=") >= 0) sh_x_e = (real) bits[++j];
			if (find(bits[j], "sh_y=") >= 0) sh_y = (real) bits[++j];
			if (find(bits[j], "sh_y_e=") >= 0) sh_y_e = (real) bits[++j];
			if (find(bits[j], "sh_z=") >= 0) sh_z = (real) bits[++j];
			if (find(bits[j], "sh_z_e=") >= 0) sh_z_e = (real) bits[++j];
			if (find(bits[j], "rot_z=") >= 0) rot_z = (real) bits[++j];
			if (find(bits[j], "rot_z_e=") >= 0) rot_z_e = (real) bits[++j];
		}
	
		if (id_raw < 0)
			continue;

		if (det_node)
		{
			int id = RawToDecSensorId(id_raw);
			a.sensorType[id] = SensorTypeFromRawId(id_raw);

			a.shr[id] = sh_r;
			a.shr_e[id] = sh_r_e;

			a.shx[id] = sh_x;
			a.shx_e[id] = sh_x_e;
			a.shy[id] = sh_y;
			a.shy_e[id] = sh_y_e;
			a.shz[id] = sh_z;
			a.shz_e[id] = sh_z_e;

			a.rotz[id] = rot_z;
			a.rotz_e[id] = rot_z_e;
		} else {
			int id = RawToDecRPId(id_raw);
			a.sensorType[id] = "RP";

			a.rp_shx[id] = sh_x;
			a.rp_shx_e[id] = sh_x_e;
			a.rp_shy[id] = sh_y;
			a.rp_shy_e[id] = sh_y_e;
			a.rp_rotz[id] = rot_z;
			a.rp_rotz_e[id] = rot_z_e;
		}
	}
	
	return 0;
}

//----------------------------------------------------------------------------------------------------

real GetQuantity(Alignment a, string qn, int key)
{
	if (qn == "shr") return a.shr[key];
	if (qn == "shr_e") return a.shr_e[key];

	if (qn == "shx") return a.shx[key];
	if (qn == "shx_e") return a.shx_e[key];

	if (qn == "shy") return a.shy[key];
	if (qn == "shy_e") return a.shy_e[key];

	if (qn == "rotz") return a.rotz[key];
	if (qn == "rotz_e") return a.rotz_e[key];

	if (qn == "rp_shx") return a.rp_shx[key];
	if (qn == "rp_shx_e") return a.rp_shx_e[key];

	if (qn == "rp_shy") return a.rp_shy[key];
	if (qn == "rp_shy_e") return a.rp_shy_e[key];

	if (qn == "rp_rotz") return a.rp_rotz[key];
	if (qn == "rp_rotz_e") return a.rp_rotz_e[key];

	return 13;
}
