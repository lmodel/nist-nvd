package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Logical grouping of CPE match criteria for affected software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CPEConfiguration  {

  private String configurationId;
  private String configurationType;
  private String operator;
  private List<CPEConfiguration> children;
  private List<CPEMatch> matches;
  private String summary;

}