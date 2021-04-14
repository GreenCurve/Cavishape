import os
import subprocess
import csv
import shutil
import json
import configparser

class Operation(object):
    global dirPath
    def Sets(key,value):
        conf = {}
        with open('config.json', 'r') as file:
            conf = json.load(file)
        conf[key] = value
        with open('config.json','w') as file:
            file.write(json.dumps(conf))
    def lsr(self):
        with open('config.json', 'r') as file:
            conf2 = {}
            conf2 = json.load(file)
            notconf = []
            for key in conf2:
                notconf.append(key)
        return notconf
    def Bmg(key):
        with open('config.json', 'r') as file:
            conf1 = {}
            conf1 = json.load(file)
        return conf1[key]
    dirPath = str(Bmg("dirPath"))
    def getColumnValues(columnTitle):
        with open('ligandEnergy.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            valuesCheck = False
            dlmtrPos = 0
            values = []
            for row in reader:
                if valuesCheck:
                    values.append(str(row[dlmtrPos:dlmtrPos + 1])[2:-2])
                else:
                    dlmtrPos = 0
                    for cell in row:
                        if str(cell).find(columnTitle) != -1:
                            valuesCheck = True
                            break
                        dlmtrPos += 1
        return values
    def Docking(structure, ligand, reference, protein, water, settings, dockingRepeats):
        try:
            os.makedirs(dirPath + r'\workbench')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\input\structures')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\input\ligands')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\input\references')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\input\proteins')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\input\settings')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\output')
        except FileExistsError: pass
        try:
            os.makedirs(dirPath + r'\output')
        except FileExistsError: pass
        os.chdir(dirPath)
        try:
            shutil.copy(dirPath + '\\input\\settings\\' + settings, dirPath + '\\workbench\\' + settings)
            shutil.copy(dirPath + '\\input\\structures\\' + structure, dirPath + '\\workbench\\' + structure)
            shutil.copy(dirPath + '\\input\\references\\' + reference, dirPath + '\\workbench\\' + reference)
            shutil.copy(dirPath + '\\input\\proteins\\' + protein, dirPath + '\\workbench\\' + protein)
            try:
                shutil.copy(dirPath + '\\input\\ligands\\' + ligand, dirPath + '\\workbench\\' + ligand)
            except FileNotFoundError: pass
            command1 = 'build_model -set ' + settings + ' -f '+ structure + ' -olog '+ structure[:-4] + '.log -oref ' + structure[:-4] + '-rfLi.pdb' ' -olig ligandSelf.mol -omm ' + structure[:-4] + '-sb.pdb -pH 7'
            command2 = 'leadfinder -grid -og gridmap.bin -mm ' + (structure[:-4] + '-sb.pdb' if protein == '' else protein) + ' -lr ' + (structure[:-4] + '-rfLi.pdb' if reference == "" else reference) + ' ' + ('-fw ' + water if water != '' else '') + ' -xp'
            command3 = 'leadfinder -g gridmap.bin -mm ' + (structure[:-4] + '-sb.pdb' if protein == '' else protein) + ' -li ' + ligand[:-4] + ' -l report.log -o ligand_docked.pdb -lr ' + (structure[:-4] + '-rfLi.pdb' if reference == "" else reference)  + ' -os ligandEnergy.csv -xp'
            SummaryMap = []
            k = 1
            g = 1
            try:
                os.makedirs(dirPath + '\\output\\' + structure[:-4] + ' ' + ligand[:-4] + ' ' + (protein[:-4] if protein != '' else '-') + ' ' + (reference[:-4] if reference != '' else '-'))
                out = dirPath + '\\output\\' + structure[:-4] + ' ' + ligand[:-4] + ' ' + (protein[:-4] if protein != '' else '-') + ' ' + (reference[:-4] if reference != '' else '-')
            except FileExistsError:
                while g == 1:
                    try:
                        os.makedirs(dirPath + '\\output\\' + structure[:-4] + ' ' + ligand[:-4] + ' ' + (protein[:-4] if protein != '' else '-') + ' ' + (reference[:-4] if reference != '-' else '-') + ' ' +  str(k))
                        out = dirPath + '\\output\\' + structure[:-4] + ' ' + ligand[:-4] + ' ' + (protein[:-4] if protein != '' else '-') + ' ' + (reference[:-4] if reference != '-' else '-') + ' ' +  str(k)
                    except:
                        k += 1
                    else: break
            os.chdir(dirPath + '\\workbench')
            subprocess.run(command1)
            for i in range(dockingRepeats):
                os.chdir(dirPath + '\\workbench')
                subprocess.run(command2)
                subprocess.run(command3)

                grids = [['Poses' + ', report N' + str(i), 'dG, kcal/mol', 'RMS, A', 'Grid Type']]
                substr = 'Grid'
                count = 0
                for count in range(len(Operation.getColumnValues('dG, kcal/mol'))):
                    subgrid = []
                    subgrid.append(str(count))
                    subgrid.append(Operation.getColumnValues('dG, kcal/mol')[count])
                    subgrid.append(Operation.getColumnValues('RMS, A')[count])
                    grids.append(subgrid)
                count = 0
                with open('report.log', 'rt') as file:
                    for line in file:
                        if count < len(Operation.getColumnValues('dG, kcal/mol')) and line.find(substr) != -1:
                            grids[count+1].append(line[:-1] if line.find(substr) != -1 else '')
                            check = False
                            for index in range(len(SummaryMap)):
                                if SummaryMap[index][0] == line:
                                    SummaryMap[index][1] += float(Operation.getColumnValues('dG, kcal/mol')[count])
                                    SummaryMap[index][2] += 1
                                    check = True
                            if not check:
                                appendLine = []
                                appendLine.append(line)
                                appendLine.append(float(Operation.getColumnValues('dG, kcal/mol')[count]))
                                appendLine.append(1)
                                SummaryMap.append(appendLine)
                            count += 1
                try:
                    os.makedirs(out + r'\primary')
                except FileExistsError:
                    pass
                try:
                    os.makedirs(out + r'\secondary')
                except FileExistsError:
                    pass
                with open(out + '\\primary\\Summary.csv','a') as file:
                    writer = csv.writer(file)
                    writer.writerows(grids)
                if i == dockingRepeats:
                    os.chdir(dirPath)
                    os.rename(dirPath + '\\workbench\\gridmap.bin', out + '\\primary\\gridmap.bin'  )
                    try:
                        os.rename(dirPath + '\\workbench\\ligandSelf.mol', out + '\\primary\\ligandSelf.mol' )
                    except FileNotFoundError: pass
                    os.rename(dirPath + '\\workbench\\' + (structure[:-4] + '-rfLi.pdb' if reference == "" else reference), out + '\\primary\\' + (structure[:-4] + '-rfLi.pdb' if reference == "" else reference))
                    os.rename(dirPath + '\\workbench\\' + (structure[:-4] + '-sb.pdb' if protein == '' else protein), out + '\\primary\\'+ (structure[:-4] + '-sb.pdb' if protein == '' else protein))

                else:
                    os.remove(dirPath + "\\workbench\\gridmap.bin")
                os.chdir(dirPath)
                os.rename(dirPath + '\\workbench\\report.log', out + '\\secondary\\report-' + str(i) + '.log')
                os.rename(dirPath + '\\workbench\\ligand_docked.pdb', out + '\\secondary\\ligand_docked-' + str(i) + '.pdb')
                os.rename(dirPath + '\\workbench\\ligandEnergy.csv', out + '\\secondary\\docking_energy-' + str(i) + '.csv')

            with open(out + '\\primary\\Summary.csv','a') as file:
                    writer = csv.writer(file)
                    writer.writerows(SummaryMap)
        except Exception:
            print('Alarm')
        finally:
            if ligand != 'ligandSelf.mol':
                os.remove(dirPath + '\\workbench\\LigandSelf.mol')
            if reference != "":
                os.remove(dirPath + '\\workbench\\' + structure[:-4] + '-rfLi.pdb')
            if protein != "":
                os.remove(dirPath + '\\workbench\\' + structure[:-4] + '-sb.pdb')
            for files in os.listdir(dirPath + '\\workbench'):
                path = os.path.join(dirPath + '\\workbench', files)
                try:
                    os.rename(dirPath + '\\workbench\\' + files, out + '\\primary\\' + files + files[-4:])
                except OSError:
                    os.rename(dirPath + '\\workbench\\' + files, out + '\\primary\\' + files + 'OhNO')

    def Extracting(structure, settings):
        try:
            os.makedirs(dirPath + r'\workbench')
        except FileExistsError:
            pass
        try:
            os.makedirs(dirPath + r'\input\structures')
        except FileExistsError:
            pass
        try:
            os.makedirs(dirPath + r'\input\ligands')
        except FileExistsError:
            pass
        try:
            os.makedirs(dirPath + r'\input\settings')
        except FileExistsError:
            pass
        try:
            os.makedirs(dirPath + r'\output')
        except FileExistsError:
            pass
        try:
            os.makedirs(dirPath + r'\output')
        except FileExistsError:
            pass
        try:
            shutil.copy(dirPath + '\\input\\settings\\' + settings, dirPath + '\\workbench\\' + settings)
            shutil.copy(dirPath + '\\input\\structures\\' + structure, dirPath + '\\workbench\\' + structure)
            os.chdir(dirPath + '\\workbench')
            command1 = 'build_model -set ' + settings + ' -f ' + structure + ' -olog ' + structure[:-4] + '.log -oref ' + structure[:-4] + '-rfLi.pdb -olig ligandSelf-' + structure[:-4] + '.mol -omm ' + structure[:-4] + '-sb.pdb -pH 7'
            subprocess.run(command1)
            g = 1
            k = 1
            try:
                os.makedirs(dirPath + '\\output\\' + structure[:-4] + ' ' + ' Ref')
                out = dirPath + '\\output\\' + structure[:-4] + ' ' + ' Ref'
            except FileExistsError:
                while g == 1:
                    try:
                        os.makedirs(dirPath + '\\output\\' + structure[:-4] + ' ' + ' Ref' + ' ' + str(k))
                        out = dirPath + '\\output\\' + structure[:-4] + ' ' + ' Ref' + ' ' + str(k)
                    except:
                        k += 1
                    else:
                        break
            os.chdir(dirPath)
            os.rename(dirPath + '\\workbench\\' + structure[:-4] + '-rfLi.pdb',out + '\\' + structure[:-4] + '-rfLi.pdb')
            os.rename(dirPath + '\\workbench\\' + structure[:-4] + '-sb.pdb', out + '\\' + structure[:-4] + '-sb.pdb')
            os.rename(dirPath + '\\workbench\\' + 'ligandSelf-' + structure[:-4] + '.mol', out + '\\' + 'ligandSelf-' + structure[:-4] + '.mol.mol')
        except Exception:
            print('Alarm')
        finally:
            for files in os.listdir(dirPath + '\\workbench'):
                path = os.path.join(dirPath + '\\workbench', files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)