import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class IfacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ifacets')

class IfacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        if package_type == 'GTN-P-dataset':
          facets_dict.clear()
          facets_dict['country'] = plugins.toolkit._('Countries')
          facets_dict['site'] = plugins.toolkit._('Sites')
          facets_dict['permafrost_zone'] = plugins.toolkit._('Permafrost Zones')
          facets_dict['vegetation_type'] = plugins.toolkit._('Vegetation Types')
          facets_dict['measure_type'] = plugins.toolkit._('Types')
          facets_dict['measure_variable'] = plugins.toolkit._('Variables')
          facets_dict['tags'] = plugins.toolkit._('Keywords')
          facets_dict['res_format'] = plugins.toolkit._('Data Formats')
          facets_dict['author'] = plugins.toolkit._('Data Authors')
          facets_dict['institute'] = plugins.toolkit._('Institutes')

          return facets_dict

        else:
          facets_dict.clear()
          facets_dict['region'] = plugins.toolkit._('Regions')
          facets_dict['product'] = plugins.toolkit._('Products')
          facets_dict['sensor'] = plugins.toolkit._('Sensors')
          facets_dict['s_resolution'] = plugins.toolkit._('Spatial Resolution')
          facets_dict['temp_resolution'] = plugins.toolkit._('Temporal Resolution')
          facets_dict['tags'] = plugins.toolkit._('Keywords')
          facets_dict['res_format'] = plugins.toolkit._('Data Formats')
          facets_dict['first_author'] = plugins.toolkit._('First Authors')
          facets_dict['groups'] = plugins.toolkit._('Projects')
          facets_dict['institute'] = plugins.toolkit._('Institutes')
          facets_dict['organization'] = plugins.toolkit._('Publishers')

          return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict.clear()
        facets_dict['region'] = plugins.toolkit._('Regions')
        facets_dict['product'] = plugins.toolkit._('Products')
        facets_dict['sensor'] = plugins.toolkit._('Sensors')
        facets_dict['s_resolution'] = plugins.toolkit._('Spatial Resolution')
        facets_dict['temp_resolution'] = plugins.toolkit._('Temporal Resolution')
        facets_dict['tags'] = plugins.toolkit._('Keywords')
        facets_dict['res_format'] = plugins.toolkit._('Data Formats')
        facets_dict['first_author'] = plugins.toolkit._('First Authors')
        facets_dict['groups'] = plugins.toolkit._('Projects')
        facets_dict['institute'] = plugins.toolkit._('Institutes')
        facets_dict['organization'] = plugins.toolkit._('Publishers')

        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict.clear()

        facets_dict['region'] = plugins.toolkit._('Regions')
        facets_dict['product'] = plugins.toolkit._('Products')
        facets_dict['sensor'] = plugins.toolkit._('Sensors')
        facets_dict['s_resolution'] = plugins.toolkit._('Spatial Resolution')
        facets_dict['temp_resolution'] = plugins.toolkit._('Temporal Resolution')
        facets_dict['tags'] = plugins.toolkit._('Keywords')
        facets_dict['res_format'] = plugins.toolkit._('Data Formats')
        facets_dict['first_author'] = plugins.toolkit._('First Authors')
        facets_dict['groups'] = plugins.toolkit._('Projects')
        facets_dict['institute'] = plugins.toolkit._('Institutes')
        facets_dict['organization'] = plugins.toolkit._('Publishers')

        return facets_dict
